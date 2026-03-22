import os
import re
from tqdm import tqdm

input_folder='data/extracted_text'
output_folder='data/cleaned_text'

os.makedirs(output_folder,exist_ok=True)

def clean_text(text):
    # Remove dotted lines
    text = re.sub(r"\.{2,}", " ", text)

    # Remove TABLE OF CONTENTS block
    text = re.sub(r"TABLE OF CONTENTS.*?(SECTION|\Z)", " ", text, flags=re.IGNORECASE)

    # Remove section numbering like "Section 200"
    text = re.sub(r"Section\s+\d+", " ", text, flags=re.IGNORECASE)

    # Remove standalone numbers and repeated numbers
    text = re.sub(r"\b\d+\b(\s+\b\d+\b)+", " ", text)
    text = re.sub(r"\b\d+\b", " ", text)

    # Remove patterns like ".14" or ". 21"
    text = re.sub(r"\.\s*\d+", " ", text)

    # Fix ALL CAPS words → normal case
    text = text.lower()
    text = text.capitalize()

    # Remove weird characters
    text = re.sub(r"[^\w\s\.,;:\-\(\)]", "", text)

    # Normalize spaces
    text = re.sub(r"\s+", " ", text)

    # Fix merged words (basic)
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

    return text.strip()

for file in tqdm(os.listdir(input_folder)):
    if file.endswith('.txt'):
        input_path=os.path.join(input_folder,file)

        with open(input_path,'r',encoding='utf-8') as f:
            text=f.read()

            cleaned=clean_text(text)
            output_file=file.replace('.txt','_clean.txt')
            output_path=os.path.join(output_folder,output_file)

            with open(output_path,'w', encoding='utf-8') as f:
                f.write(cleaned)

print("Text cleaning completed.")   
with open("data/cleaned_text/Emplolyee Handbook_clean.txt") as f:
    print(f.read()[:1000])