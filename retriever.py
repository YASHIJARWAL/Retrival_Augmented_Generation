from sentence_transformers import (
    SentenceTransformer
)
import os 
from dotenv import load_dotenv

from qdrant_client import QdrantClient

from rank_bm25 import BM25Okapi

import numpy as np
load_dotenv()


COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = QdrantClient(
    path = os.getenv("QDRANT_DATA")
)

embedding_model = SentenceTransformer(
    os.getenv("EMBEDDING_MODEL")
)


class HybridRetriever:

    def __init__(self):
        self.documents = []
        self.tokenized_docs = []
        self.bm25 = None

        self.load_documents()

    def load_documents(self):
        collections = (
            client.get_collections()
            .collections
        )

        collection_names = [
            c.name for c in collections
        ]

        if COLLECTION_NAME not in collection_names:
            raise Exception(
                f"Collection '{COLLECTION_NAME}' "
                "does not exist. "
                "Run ingest.py first."
            )

        records, _ = client.scroll(
            collection_name=COLLECTION_NAME,
            limit=10000,
            with_payload=True
        )

        for r in records:
            text = r.payload["text"]

            self.documents.append({
                "text": text,
                "page": r.payload["page"]
            })

        self.tokenized_docs = [
            doc["text"].split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(
            self.tokenized_docs
        )

    def semantic_search(self, query, k=5):
        query_vector = embedding_model.encode(
            query
        ).tolist()

        results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=k
        )

        return [
            {
                "text": r.payload["text"],
                "page": r.payload["page"]
            }
            for r in results
        ]

    def keyword_search(self, query, k=5):
        tokenized_query = query.split()

        scores = self.bm25.get_scores(
            tokenized_query
        )

        top_indices = np.argsort(
            scores
        )[::-1][:k]

        return [
            self.documents[i]
            for i in top_indices
        ]

    def hybrid_search(self, query):
        semantic = self.semantic_search(
            query
        )

        keyword = self.keyword_search(
            query
        )

        combined = semantic + keyword

        unique = []

        seen = set()

        for item in combined:
            key = item["text"][:100]

            if key not in seen:
                seen.add(key)
                unique.append(item)

        return unique[:5]