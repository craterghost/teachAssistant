import pdftotext
import re
import random
import argparse
from tqdm import tqdm
from difflib import SequenceMatcher
from transformers import pipeline

#############################
# How similar questions can be
similarity = 0.8

# How many chunks of data should be used for that test (-1 for no limit => whole documents)
num_chunks = 2

# Number of considered signs per question
chunk_size = 4000

##############################

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate flashcards from a PDF document.')
parser.add_argument('pdf_file', metavar='PDF_FILE', type=str,
                    help='path to the PDF file to be processed')
args = parser.parse_args()

# Load your PDF
with open(args.pdf_file, "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?
#print(len(pdf))

# Iterate over all the pages
#for page in pdf:
#    print(page)

# Read some individual pages
#print(pdf[0])
#print(pdf[1])

# Read all the text into one string
#print("\n\n".join(pdf))

# Save all text to a variable
text_long = "\n\n".join(pdf)
#################################
# Cut text into 2000 character chunks and put the chunks into a list.
chunk_list = [text_long[i:i+chunk_size] for i in range(0, len(text_long), chunk_size)]

# Use only the first x elements of the chunk list
chunk_list = chunk_list[:num_chunks]

# Print the list
#print(chunk_list)
#############################################

# Set up the text generation pipeline using the "text2text-generation" task
generator = pipeline(
    "text2text-generation",
    model="dbmdz/bert-base-german-uncased",
    device=0,
    timeout=600  # Increase the timeout to 10 minutes (in seconds)
)

def generate_flashcards(chunk, existing_questions):
    # Clean the input chunk
    clean_chunk = re.sub(r"\s+", " ", chunk.strip())

    # Generate a question using the Hugging Face pipeline
    question = generator(f"Generiere eine spezifische technische Postgrad-Level Frage basierend auf folgendem Text:\n\n{clean_chunk}\n\n", max_length=200)[0]["generated_text"].strip()

    # Check if the question is too similar to existing questions
    if any(SequenceMatcher(None, question, existing_question).ratio() > similarity for existing_question in existing_questions):
        # If the question is too similar, generate a new question
        return None
    
    # Generate an answer using the Hugging Face pipeline
    answer = generator(f"\n\n{question}\n\n Antworte einfach, technisch und spezifisch.", max_length=400)[0]["generated_text"].strip()

    return {"question": question, "answer": answer}

###############################################
# Create an empty list to store the question answer pairs
question_answer_list = []

# Create a set to store existing questions
existing_questions = set()

# Create a progressbar
progress_bar = tqdm(total=len(chunk_list))

# Define a function to generate flashcards for a single chunk
def generate_flashcards_for_chunk(chunk):
    # Generate 5 flashcards
    num_flashcards = 2
    flashcards_generated = 0
    while flashcards_generated < num_flashcards:
        # Generate a flashcard
        flashcard = generate_flashcards(chunk, existing_questions)
        if flashcard is not None:
            # If the flashcard is not None, add it to the list
            question_answer_list.append(flashcard)
            existing_questions.add(flashcard["question"])
            flashcards_generated += 1
        # Update the progress bar
        progress_bar.update(1)

