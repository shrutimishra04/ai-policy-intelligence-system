import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
from rank_bm25 import BM25Okapi
import re

# ---------------------------
# Load Model
# ---------------------------
model = SentenceTransformer("BAAI/bge-small-en")

# ---------------------------
# Load FAISS Index
# ---------------------------
index = faiss.read_index("data/faiss_index/index.faiss")

# ---------------------------
# Load Chunks
# ---------------------------
with open("data/faiss_index/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


# ---------------------------
# TEXT PREPROCESSING (FIX 1)
# ---------------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()


# ---------------------------
# BM25 SETUP (FIX 1)
# ---------------------------
tokenized_corpus = [preprocess(chunk) for chunk in chunks]
bm25 = BM25Okapi(tokenized_corpus)


# ---------------------------
# FAISS SEARCH
# ---------------------------
def faiss_search(query, k=10):   # FIX 3 → increased k
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(chunks):
            results.append(chunks[i])

    return results


# ---------------------------
# BM25 SEARCH
# ---------------------------
def bm25_search(query, k=10):   # FIX 3 → increased k
    tokenized_query = preprocess(query)
    scores = bm25.get_scores(tokenized_query)

    ranked_indices = np.argsort(scores)[::-1][:k]

    results = [chunks[i] for i in ranked_indices]
    return results


# ---------------------------
# HYBRID SEARCH (MAIN)
def retrieve(query, k=5):

    expanded_query = query + " leave policy employee benefits paid leave HR rules"

    faiss_results = faiss_search(expanded_query, k=10)
    bm25_results = bm25_search(expanded_query, k=10)

    combined = []
    seen = set()

    for chunk in faiss_results + bm25_results:
        if chunk not in seen:
            combined.append(chunk)
            seen.add(chunk)

    # simple semantic re-ranking using embeddings
    query_embedding = model.encode([query]).astype("float32")
    faiss.normalize_L2(query_embedding)

    chunk_embeddings = model.encode(combined).astype("float32")
    faiss.normalize_L2(chunk_embeddings)

    scores = np.dot(chunk_embeddings, query_embedding.T).reshape(-1)

    ranked_indices = np.argsort(scores)[::-1]

    reranked = [combined[i] for i in ranked_indices]

    return reranked[:k]

    # print("\n--- DEBUG: Retrieved Chunks ---\n")
    # for i, chunk in enumerate(combined[:5]):
    #     print(f"{i+1}. {chunk[:200]}\n")

    # return final_chunks[:k]