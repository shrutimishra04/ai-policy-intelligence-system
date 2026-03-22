import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_file = os.path.join(BASE_DIR, 'data/chunks/chunks.json')
embedding_folder = os.path.join(BASE_DIR, 'data/embeddings')
vectorestore_folder = os.path.join(BASE_DIR, 'data/vectorstore')

print("Base dir:", BASE_DIR)
print("Embeddings will be saved in:", embedding_folder)
print("FAISS index will be saved in:", vectorestore_folder)

os.makedirs(embedding_folder,exist_ok=True)
os.makedirs(vectorestore_folder,exist_ok=True)

#load chunks
with open(input_file,'r',encoding='utf-8') as f:
    chunks=json.load(f)

texts=[chunk['text'] for chunk in chunks]

print('Loading embedding model...')

#model
model=SentenceTransformer('BAAI/bge-small-en')
print('Generating embeddings...')

embeddings=model.encode(texts, show_progress_bar=True)
embeddings=np.array(embeddings).astype('float32')

#save embeddings
np.save(os.path.join(embedding_folder,'embeddings.npy'), embeddings)

#Create FAISS index
dimension=embeddings.shape[1]

index=faiss.IndexFlatL2(dimension)
index.add(embeddings)

#save FAISS index
faiss.write_index(index, os.path.join(vectorestore_folder,'faiss_index'))   

print("Embeddings + FAISS index created successfully!")
print("Total vectors:", len(embeddings))