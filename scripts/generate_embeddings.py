import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_file = os.path.join(BASE_DIR, 'data/chunks/chunks.json')
output_folder = os.path.join(BASE_DIR, 'data/faiss_index')

os.makedirs(output_folder, exist_ok=True)

# load chunks
with open(input_file, 'r', encoding='utf-8') as f:
    chunks = json.load(f)

texts = [chunk['text'] for chunk in chunks]

print('Loading embedding model...')

model = SentenceTransformer('BAAI/bge-small-en')

print('Generating embeddings...')

embeddings = model.encode(texts, show_progress_bar=True)
embeddings = np.array(embeddings).astype('float32')

# normalize embeddings (important for similarity)
faiss.normalize_L2(embeddings)

# create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)  # better for cosine similarity
index.add(embeddings)

# save FAISS index
faiss.write_index(index, os.path.join(output_folder, 'index.faiss'))

# save chunks for retrieval
import pickle
with open(os.path.join(output_folder, 'chunks.pkl'), 'wb') as f:
    pickle.dump(texts, f)

print("Embeddings + FAISS index created successfully!")
print("Total vectors:", len(embeddings))