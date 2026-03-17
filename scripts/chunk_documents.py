import os
import json
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter

input_folder='data/cleaned_text'
output_folder='data/chunks'

os.makedirs(output_folder,exist_ok=True)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=100)

all_chunks=[]

def  split_sections(text):
    """
    Split document by section headings
    """
    sections = re.split(r'\n[A-Z][A-Z\s]{3,}\n', text)
    return sections

for file in os.listdir(input_folder):
    if file.endswith('.txt'):
        path=os.path.join(input_folder,file)

        with open(path,'r',encoding='utf-8') as f:
            text=f.read()

        sections=split_sections(text)

        for section_id, section in enumerate(sections):
            chunks=splitter.split_text(section)

            for i, chunk in enumerate(chunks):
                all_chunks.append({
                    "doc_name": file.replace("_clean.txt", ""),
                    "section_id": section_id,
                    "chunk_id": i,
                    "text": chunk
                })

output_file=os.path.join(output_folder,'chunks.json')

with open(output_file,'w',encoding='utf-8') as f:
    json.dump(all_chunks,f,indent=2)

print("Document chunking completed.")
print("Total chunks:", len(all_chunks))