from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_rag

app = FastAPI()


class Query(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Rust RAG API running"
    }


@app.post("/ask")
def ask(query: Query):
    result = ask_rag(
        query.question
    )

    return result