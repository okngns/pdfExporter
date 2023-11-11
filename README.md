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
   
## Sample Output

Below is a sample DataFrame output containing named entities extracted from each PDF file:
```
        Entity      Type
1          2018      DATE
2          2019      DATE
3        61,550  CARDINAL
4        63,341  CARDINAL
5           2.9  CARDINAL
...         ...       ...
126656  Cluj-Napoca       ORG
126657  Cluj-Napoca       ORG
126658  Cluj-Napoca       ORG
126659           68  CARDINAL
126660           69  CARDINAL
```



