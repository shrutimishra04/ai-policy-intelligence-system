import os
import faiss
import numpy as np
import pickle

# Create folder if not exists
os.makedirs("data/faiss_index", exist_ok=True)

# Load embeddings
embeddings = np.load("data/embeddings/embeddings.npy")

# Load chunks
with open("data/chunks/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

embeddings = embeddings.astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Save index
faiss.write_index(index, "data/faiss_index/index.faiss")

print("✅ FAISS index saved!")

# Save chunks
with open("data/faiss_index/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ Chunks saved!")