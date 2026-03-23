import fitz  # PyMuPDF
import os
from tqdm import tqdm
import re

input_folder = "data/raw_pdfs"
output_folder = "data/extracted_text"

os.makedirs(output_folder, exist_ok=True)


# ---------------------------
# CLEANING FUNCTION
# ---------------------------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)   # normalize spaces
    text = text.strip()
    return text


# ---------------------------
# PDF EXTRACTION FUNCTION
# ---------------------------
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    final_text = ""

    for page in doc:
        blocks = page.get_text("blocks")  # structured extraction

        for block in blocks:
            block_text = block[4].strip()

            # ---------------------------
            # FILTER NOISE
            # ---------------------------
            if len(block_text) < 40:
                continue  # skip tiny useless text

            if any(x in block_text.lower() for x in [
                "table of content",
                "page ",
                "copyright",
                "rc ",
                "date:"
            ]):
                continue

            final_text += block_text + "\n\n"   # keep structure

    return final_text


# ---------------------------
# MAIN PROCESS
# ---------------------------
for pdf_file in tqdm(os.listdir(input_folder)):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, pdf_file)

        text = extract_text_from_pdf(pdf_path)
        text = clean_text(text)

        txt_name = pdf_file.replace(".pdf", ".txt")
        txt_path = os.path.join(output_folder, txt_name)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)


print("Text extraction completed.")


# ---------------------------
# DEBUG SAMPLE OUTPUT
# ---------------------------
sample_file = os.listdir(output_folder)[0]
with open(os.path.join(output_folder, sample_file), encoding="utf-8") as f:
    print("\n--- SAMPLE OUTPUT ---\n")
    print(f.read()[:1000])
            