import os
import re
from tqdm import tqdm

input_folder='data/extracted_text'
output_folder='data/cleaned_text'

os.makedirs(output_folder,exist_ok=True)

def clean_text(text):
    # Remove dotted lines like .............
    text = re.sub(r"\.{2,}", " ", text)

    # Remove page numbers at end of lines
    text = re.sub(r"\s+\d+\s*$", "", text, flags=re.MULTILINE)

    # Remove standalone numbers
    text = re.sub(r"\n\d+\n", "\n", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove weird characters
    text = re.sub(r"[^\w\s\.,;:\-\(\)]", "", text)

    # Normalize spaces again
    text = re.sub(r"\s+", " ", text)

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