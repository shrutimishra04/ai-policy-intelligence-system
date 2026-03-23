import os
import json
import re
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter

input_folder = 'data/extracted_text'
output_folder = 'data/chunks'

os.makedirs(output_folder, exist_ok=True)


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " "]
)

all_chunks = []

for file in tqdm(os.listdir(input_folder)):
    if file.endswith('.txt'):
        path = os.path.join(input_folder, file)

        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        text = clean_text(text)

        chunks = splitter.split_text(text)

        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) < 50:
                continue

            all_chunks.append({
                "doc_name": file.replace(".txt", ""),
                "chunk_id": i,
                "text": chunk.strip()
            })


output_file = os.path.join(output_folder, 'chunks.json')

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_chunks, f, indent=2)


print("Document chunking completed.")
print("Total chunks:", len(all_chunks))