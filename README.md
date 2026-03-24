# AI Policy Intelligence System (RAG-based HR Assistant)

## Overview
This project is a Retrieval-Augmented Generation (RAG) based HR Policy Assistant that answers user queries from real-world HR policy documents.

The system processes multiple HR PDFs and allows users to ask questions like:
- "What is the leave policy?"
- "How many paid leaves per year?"
- "What are employee leave rules?"

It retrieves relevant policy content and generates accurate, context-grounded answers.

---

## Features

- Hybrid Search (FAISS + BM25)
- Semantic + Keyword Retrieval
- Re-ranking for improved accuracy
- LLM-based Answer Generation
- FastAPI Backend
- Interactive Chat UI (HTML + JS)
- Chat History using localStorage

---

## Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers (bge-small-en)
- BM25 (rank-bm25)
- OpenAI API (GPT-4o-mini)
- HTML, CSS, JavaScript

---

## Project Structure


AI Policy Intelligence System/
│
├── api/
│ └── main.py # FastAPI backend
│
├── rag/
│ ├── retriever.py # Hybrid search + reranking
│ ├── generator.py # LLM answer generation
│ └── rag_pipeline.py # Full pipeline
│
├── scripts/
│ ├── extract_text.py # PDF text extraction
│ ├── chunk_documents.py # Chunking logic
│ └── generate_embeddings.py# Embeddings + FAISS
│
├── data/
│ ├── raw_pdfs/
│ ├── extracted_text/
│ ├── chunks/
│ └── faiss_index/
│
├── ui/
│ └── index.html # Chat UI
│
└── README.md


---

## System Architecture


PDFs → Extraction → Chunking → Embeddings → FAISS Index

<<<<<<< HEAD
3. Text Cleaning  
   Removes noise such as page numbers, formatting artifacts, and unwanted characters  

4. Document Chunking  
   Splits documents into smaller chunks using a recursive text splitter  
   Section-aware chunking is used to preserve policy context  

5. Embedding Generation   
   Converts text chunks into vector embeddings using sentence-transformers  

6. Vector Database 
   Stores embeddings in FAISS for efficient similarity search  

---

## Current Status

Completed:

- Data collection  
- PDF text extraction  
- Text cleaning and preprocessing  
- Section-aware document chunking  

Upcoming:

- Embedding generation  
- FAISS vector database  
- Query and retrieval system  
- API and UI integration  

---

## How to Run

Run scripts from the project root:
python scripts/extract_text.py
python scripts/clean_text.py
python scripts/chunk_documents.py
=======
User Query
↓
Hybrid Search (FAISS + BM25)
↓
Re-ranking
↓
Top Chunks
↓
LLM (GPT-4o-mini)
↓
Final Answer
>>>>>>> 632d42c (Final end-to-end RAG system with FastAPI backend and frontend UI)


---

## Key Improvements & Learnings

### 1. Data Quality Matters Most
Initial poor results were due to weak PDF extraction and noisy text.

Fix:
- Structured block extraction
- Noise removal

---

### 2. Hybrid Search
FAISS alone failed for keyword queries.

Solution:
- Combined FAISS (semantic) + BM25 (keyword)

---

### 3. Chunking Strategy
Improved chunking with:
- chunk_size = 400
- overlap = 100
- better separators

---

### 4. Re-ranking
Added embedding-based re-ranking to prioritize relevant chunks.

---

### 5. Prompt Engineering
Improved LLM responses by:
- restricting answers to context
- reducing hallucination

---

## Setup Instructions

### 1. Clone Repository

git clone <your-repo-link>
cd project-folder


---

### 2. Install Dependencies

pip install -r requirements.txt


---

### 3. Run FastAPI Server

uvicorn api.main:app --reload


---

### 4. Open UI
Open:

ui/index.html


---

## API Endpoint

### POST /ask

Request:
```json
{
  "query": "leave policy"
}

Response:

{
  "answer": "Employees are entitled to..."
}
Future Improvements
Deploy on cloud (AWS / Render)
Add authentication
Add chat history backend (DB)
Improve UI with React
Add evaluation metrics

# AI Policy Intelligence System (RAG-based HR Assistant)

## Overview
This project is a Retrieval-Augmented Generation (RAG) based HR Policy Assistant that answers user queries from real-world HR policy documents.

The system processes multiple HR PDFs and allows users to ask questions like:
- "What is the leave policy?"
- "How many paid leaves per year?"
- "What are employee leave rules?"

It retrieves relevant policy content and generates accurate, context-grounded answers.

---

## Features

- Hybrid Search (FAISS + BM25)
- Semantic + Keyword Retrieval
- Re-ranking for improved accuracy
- LLM-based Answer Generation
- FastAPI Backend
- Interactive Chat UI (HTML + JS)
- Chat History using localStorage

---

## Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers (bge-small-en)
- BM25 (rank-bm25)
- OpenAI API (GPT-4o-mini)
- HTML, CSS, JavaScript

---

## Project Structure


AI Policy Intelligence System/
│
├── api/
│ └── main.py # FastAPI backend
│
├── rag/
│ ├── retriever.py # Hybrid search + reranking
│ ├── generator.py # LLM answer generation
│ └── rag_pipeline.py # Full pipeline
│
├── scripts/
│ ├── extract_text.py # PDF text extraction
│ ├── chunk_documents.py # Chunking logic
│ └── generate_embeddings.py# Embeddings + FAISS
│
├── data/
│ ├── raw_pdfs/
│ ├── extracted_text/
│ ├── chunks/
│ └── faiss_index/
│
├── ui/
│ └── index.html # Chat UI
│
└── README.md


---

## System Architecture


PDFs → Extraction → Chunking → Embeddings → FAISS Index

User Query
↓
Hybrid Search (FAISS + BM25)
↓
Re-ranking
↓
Top Chunks
↓
LLM (GPT-4o-mini)
↓
Final Answer


---

## Key Improvements & Learnings

### 1. Data Quality Matters Most
Initial poor results were due to weak PDF extraction and noisy text.

Fix:
- Structured block extraction
- Noise removal

---

### 2. Hybrid Search
FAISS alone failed for keyword queries.

Solution:
- Combined FAISS (semantic) + BM25 (keyword)

---

### 3. Chunking Strategy
Improved chunking with:
- chunk_size = 400
- overlap = 100
- better separators

---

### 4. Re-ranking
Added embedding-based re-ranking to prioritize relevant chunks.

---

### 5. Prompt Engineering
Improved LLM responses by:
- restricting answers to context
- reducing hallucination

---

## Setup Instructions

### 1. Clone Repository

git clone <your-repo-link>
cd project-folder


---

### 2. Install Dependencies

pip install -r requirements.txt


---

### 3. Run FastAPI Server

uvicorn api.main:app --reload


---

### 4. Open UI
Open:

ui/index.html


---

## API Endpoint

### POST /ask

Request:
```json
{
  "query": "leave policy"
}

Response:

{
  "answer": "Employees are entitled to..."
}
Future Improvements
Deploy on cloud (AWS / Render)
Add authentication
Add chat history backend (DB)
Improve UI with React
Add evaluation metrics

Author

Shruti Mishra 
B.Tech Graduate | Post Graduate Diploma in Artificial Intelligence 
Email: shrutim318@gmail.com

