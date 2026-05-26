import fitz
import uuid
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
load_dotenv()
PDF_PATH = os.getenv("PDF_PATH")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = QdrantClient(
    path=os.getenv("QDRANT_DATA")
)

embedding_model = SentenceTransformer(
    os.getenv("EMBEDDING_MODEL")
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=120
)


def extract_pdf():
    print("Opening PDF...")

    doc = fitz.open(PDF_PATH)

    pages = []

    for i, page in enumerate(doc):
        text = page.get_text()

        if text.strip():
            pages.append({
                "page": i + 1,
                "text": text
            })

    return pages


def create_chunks(pages):
    chunks = []

    for page in pages:
        splits = splitter.split_text(
            page["text"]
        )

        for chunk in splits:
            chunks.append({
                "id": str(uuid.uuid4()),
                "text": chunk,
                "page": page["page"]
            })

    return chunks


def create_collection():
    collections = client.get_collections().collections

    collection_names = [
        c.name for c in collections
    ]

    if COLLECTION_NAME in collection_names:
        print("Collection already exists")
        return

    print("Creating collection...")

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=1024,
            distance=Distance.COSINE
        )
    )


def ingest_chunks(chunks):
    points = []

    for i, chunk in enumerate(chunks):
        print(
            f"Embedding chunk {i+1}/{len(chunks)}",
            end="\r"
        )

        vector = embedding_model.encode(
            chunk["text"]
        ).tolist()

        points.append(
            PointStruct(
                id=chunk["id"],
                vector=vector,
                payload={
                    "text": chunk["text"],
                    "page": chunk["page"]
                }
            )
        )

    print("\nUploading to Qdrant...")

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


if __name__ == "__main__":
    print("Extracting PDF...")

    pages = extract_pdf()

    print(f"Pages extracted: {len(pages)}")

    print("Creating chunks...")

    chunks = create_chunks(pages)

    print(f"Chunks created: {len(chunks)}")

    create_collection()

    print("Ingesting vectors...")

    ingest_chunks(chunks)

    print("Done!")