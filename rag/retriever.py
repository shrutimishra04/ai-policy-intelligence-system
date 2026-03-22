import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("BAAI/bge-small-en")

# Load FAISS index
index = faiss.read_index("data/faiss_index/index.faiss")

# Load chunks
with open("data/faiss_index/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

def retrieve(query, k=5):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        if 0 <= i < len(chunks):   # safety check
            results.append(chunks[i])

    return results