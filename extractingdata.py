import fitz  # PyMuPDF
import spacy
import pandas as pd
import os

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

folder_path = 'datas'

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

# Get the paths of PDF files
pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]

all_entities = []

# Process each PDF and collect entities
for pdf_file in pdf_files:
    text = extract_text_from_pdf(pdf_file)
    
    # Process each PDF text with SpaCy
    doc = nlp(text)
    
    # Collect entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Add all entities to a list
    all_entities.extend(entities)

# Convert all entities to a DataFrame
merged_df = pd.DataFrame(all_entities, columns=['Entity', 'Type'])
# Display the results
print(merged_df)
