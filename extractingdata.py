import fitz  # PyMuPDF
import spacy
import pandas as pd
import os

# SpaCy modelini yükleyin
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

# PDF dosyalarının yollarını alın
pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]

all_entities = []

# Her bir PDF'yi işleyin ve entiteleri toplayın
for pdf_file in pdf_files:
    text = extract_text_from_pdf(pdf_file)
    
    # Her bir PDF metnini SpaCy ile işleyin
    doc = nlp(text)
    
    # Entiteleri toplayın
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Tüm entiteleri bir listeye ekleyin
    all_entities.extend(entities)

# Tüm entiteleri DataFrame'e dönüştürün
merged_df = pd.DataFrame(all_entities, columns=['Entity', 'Type'])
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Sonuçları görüntüleyin
print(merged_df)
