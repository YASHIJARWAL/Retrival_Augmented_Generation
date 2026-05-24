import requests

from retriever import HybridRetriever
from prompts import SYSTEM_PROMPT

OLLAMA_URL = (
    "http://localhost:11434/api/generate"
)

MODEL_NAME = "qwen2.5:7b"

retriever = None


def build_context(chunks):
    context = ""

    for chunk in chunks:
        context += (
            f"\n[Page {chunk['page']}]\n"
            f"{chunk['text']}\n"
        )

    return context


def ask_rag(question):
    global retriever

    if retriever is None:
        retriever = HybridRetriever()

    chunks = retriever.hybrid_search(
        question
    )

    context = build_context(chunks)

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return {
        "answer": result["response"],
        "sources": chunks
    }