# AI Policy Intelligence System (RAG-based)

This project is a Retrieval-Augmented Generation (RAG) system designed to analyze and query HR policy documents such as employee handbooks, HR manuals, and organizational policies.

The system processes multiple policy PDFs and enables semantic search over them, allowing users to retrieve relevant policy information based on natural language queries.

---

## Project Overview

Organizations maintain large policy documents that are difficult to navigate manually. This system converts those documents into a searchable knowledge base using embeddings and vector search.

The pipeline includes:

- Extracting text from PDF documents  
- Cleaning and preprocessing the text  
- Splitting documents into meaningful chunks  
- Generating embeddings for semantic understanding  
- Storing embeddings in a FAISS vector database  

---

## Folder Structure
AI Policy Intelligence System using RAG/

scripts/
extract_text.py
clean_text.py
chunk_documents.py

data/
(raw data not included in repository)


---

## Pipeline

1. Data Collection  
   HR policy PDFs are stored locally in `data/raw_pdfs/`

2. Text Extraction  
   Extracts raw text from PDFs using PyMuPDF  

3. Text Cleaning  
   Removes noise such as page numbers, formatting artifacts, and unwanted characters  

4. Document Chunking  
   Splits documents into smaller chunks using a recursive text splitter  
   Section-aware chunking is used to preserve policy context  

5. Embedding Generation *(next phase)*  
   Converts text chunks into vector embeddings using sentence-transformers  

6. Vector Database *(next phase)*  
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


---

## Notes

- Large data files (PDFs, embeddings, vector index) are not included in this repository  
- This project is designed to be extended into a full RAG-based chatbot or policy assistant  

---

## Future Improvements

- Add query interface for semantic search  
- Integrate LLM for answer generation  
- Build API using FastAPI  
- Add dashboard for visualization  

---