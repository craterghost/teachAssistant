# Teach Assistant

Teach Assistant is an AI-powered PDF information extraction tool that automates the process of generating technical questions and their corresponding answers based on a PDF document. This tool leverages OpenAI's GPT-3 model to analyze and generate questions and answers for each chunk of text in the PDF, making it a valuable resource for researchers, educators, and professionals who need to extract important information from a PDF document.

The repository includes two Jupyter notebooks:

    - teachAssistantSinglethread.ipynb: This notebook runs the code in a single thread.
    - teachAssistantMultithread.ipynb: This notebook uses multithreading to speed up the process.

## Prerequisites

Before running the code, you need to make sure you have the following:

    - Python 3.x
    - pdftotext
    - OpenAI API key
    - tqdm
    - difflib
    - concurrent.futures

To install the required packages, you can use pip:

``` pip install pdftotext openai tqdm difflib concurrent.futures ```

## How to use

To use this code, follow these steps:

    - Set your OpenAI API key in the code. You can get your API key from the OpenAI website.

    - Define the similarity threshold (similarity), the number of chunks to be used (num_chunks), the number of questions per chunk (num_questions), and the number of considered signs per question (chunk_size).

    - Load your PDF by specifying its filename.

    - Run the code.

    - The output of the code will be the generated question-answer pairs.

## Limitations

There are a few limitations to this code that are worth mentioning:

   - The quality of the generated questions and answers is highly dependent on the quality of the input text. If the text is poorly written or contains errors, the generated questions and answers may not be very useful.

   - The OpenAI API has a limit on the number of requests that can be made per month. If you exceed this limit, you will need to pay for additional requests or wait until the next month to continue using the API.

   - The code is not optimized for large PDFs. Generating questions and answers for a large PDF may take a long time and require a significant amount of memory.

   - The similarity threshold (similarity) used in the code is arbitrary and may need to be adjusted depending on the specific use case.

   - The code is not designed to handle password-protected PDFs. If the PDF is password-protected, you will need to remove the password before running the code.