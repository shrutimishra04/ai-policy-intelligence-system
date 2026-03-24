from fastapi import FastAPI
from pydantic import BaseModel
from rag.rag_pipeline import ask_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "RAG API running"}


@app.post("/ask")
def ask(request: QueryRequest):
    answer = ask_question(request.query)
    return {"answer": answer}