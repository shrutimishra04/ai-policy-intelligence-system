import os
import pickle
from PyPDF2 import PdfReader

def extract_text_from_pdfs(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, file))
            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            documents.append(text)

    return documents


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


# 👉 CHANGE THIS PATH if needed
pdf_folder = "data/raw_pdfs"

documents = extract_text_from_pdfs(pdf_folder)

all_chunks = []
for doc in documents:
    all_chunks.extend(chunk_text(doc))

print(f"Total chunks: {len(all_chunks)}")

# Save chunks
os.makedirs("data/chunks", exist_ok=True)

with open("data/chunks/chunks.pkl", "wb") as f:
    pickle.dump(all_chunks, f)

print("✅ Chunks rebuilt and saved!")