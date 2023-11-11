# PDF Entity Extractor

This Python script extracts text from PDF files and identifies named entities using the SpaCy library.

## Requirements

- Python 3.x
- SpaCy library (`pip install spacy`)
- en_core_web_sm SpaCy model (`python -m spacy download en_core_web_sm`)
- PyMuPDF library (`pip install PyMuPDF`)
- pandas library (`pip install pandas`)

## Usage

1. Install Python 3 and the required libraries.
2. Download the SpaCy model: `python -m spacy download en_core_web_sm`
3. Run the script in the project folder:

   ```bash
   python entity_extractor.py
