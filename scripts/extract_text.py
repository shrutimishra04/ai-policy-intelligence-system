import fitz
import os
from tqdm import tqdm

input_folder = "data/raw_pdfs"
output_folder = "data/extracted_text"

os.makedirs(output_folder, exist_ok=True)

for pdf_file in tqdm(os.listdir(input_folder)):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(input_folder, pdf_file)

        doc = fitz.open(pdf_path)
        text = ""

        for page in doc:
            # ✅ FIX 1: better extraction mode
            text += page.get_text("text")

        # ✅ FIX 2: basic cleaning
        text = text.replace("\n", " ")
        text = " ".join(text.split())  # remove extra spaces

        txt_name = pdf_file.replace(".pdf", ".txt")
        txt_path = os.path.join(output_folder, txt_name)

        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)

print("Text extraction completed.")

with open("data/extract_text/Emplolyee Handbook_clean.txt",encoding='utf-8') as f:
    print(f.read()[:1000])
            