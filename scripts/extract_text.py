import fitz
import os
from tqdm import tqdm

#input and output folders
input_folder="data/raw_pdfs"
output_folder="data/extracted_text"

#create output folder if it dosen't exist
os.makedirs(output_folder,exist_ok=True)

#loop through PDFs
for pdf_file in tqdm(os.listdir(input_folder)):
    if pdf_file.endswith('.pdf'):
        pdf_path=os.path.join(input_folder,pdf_file)

        #open pdf
        doc=fitz.open(pdf_path)
        text=""

        #extract page text
        for page in doc:
            text += page.get_text()

        #save as txt
        txt_name=pdf_file.replace(".pdf",".txt")
        txt_path=os.path.join(output_folder,txt_name)

        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)

print("Text extraction completed.")
            