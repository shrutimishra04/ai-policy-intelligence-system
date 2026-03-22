import os
import json
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter

input_folder = 'data/cleaned_text'
output_folder = 'data/chunks'

os.makedirs(output_folder, exist_ok=True)

# Initialize text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

all_chunks = []

for file in tqdm(os.listdir(input_folder)):
    if file.endswith('.txt'):
        path = os.path.join(input_folder, file)

        with open(path, 'r', encoding='utf-8') as f:
            text = f.read().strip()  # important

        # Generate chunks directly (no section splitting)
        chunks = splitter.split_text(text)

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "doc_name": file.replace("_clean.txt", ""),
                "chunk_id": i,
                "text": chunk
            })

# Save chunks
output_file = os.path.join(output_folder, 'chunks.json')

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_chunks, f, indent=2)

print("Document chunking completed.")
print("Total chunks:", len(all_chunks))