import fitz  
import spacy
import pandas as pd
import os

# Spacy modelini yuklemek icin kullaniyoruz
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

# PDF dosyalarindan path leri almak icin 
pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]

all_entities = []

# butun pdfleri calistir ve entiti topla
for pdf_file in pdf_files:
    text = extract_text_from_pdf(pdf_file)
    
    # PDF leri text olarak calistiriyoruz Spacy kullanarak
    doc = nlp(text)
    
    # entitileri topla
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # butun entitileri dosyaya ekle
    all_entities.extend(entities)

# butun entitileri data frame e donustur
merged_df = pd.DataFrame(all_entities, columns=['Entity', 'Type'])


print(merged_df)
