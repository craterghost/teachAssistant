#AI Document Information Extraction Tool

This AI-powered tool is designed to extract information from various document formats, including .doc and .pdf files, to create flashcards for quick and easy learning.
Features

    Extracts information from .doc and .pdf files using OCR technology
    Automatically creates flashcards with the extracted information
    Allows users to review and edit flashcards before finalizing them
    Provides options for customizing flashcard templates and settings
    Supports multiple languages and character sets

##Requirements

    Python 3.7 or higher
    Pip package manager
    Required Python libraries:
        pytesseract
        pillow
        docx2txt
        fpdf
        nltk

##Installation

    - Clone the repository to your local machine

    - Install the required Python libraries using pip:

```
pip install pytesseract pillow docx2txt fpdf nltk
```

Download the necessary language data for NLTK:

python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger

Run the main.py file to start the tool:

css

    python main.py

Usage

    Launch the tool by running main.py
    Select the document file(s) to extract information from (supported file types include .doc and .pdf)
    Choose the flashcard template and settings (font, font size, background color, etc.)
    Review and edit the extracted information, if necessary
    Generate the flashcards and save them to a PDF file for printing or sharing

Limitations

    The accuracy of the information extraction is dependent on the quality of the document and the OCR technology used
    The tool may not work as expected for documents with complex layouts or fonts that are not recognized by the OCR engine
    The flashcard templates are limited and may not suit all users' preferences and needs
    The tool does not support other document formats beyond .doc and .pdf files

Credits

This tool was developed by [Your Name] using various open-source libraries and technologies, including:

    Tesseract OCR
    Pillow
    docx2txt
    FPDF
    NLTK
