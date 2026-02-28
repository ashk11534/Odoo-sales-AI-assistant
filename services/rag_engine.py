from sentence_transformers import SentenceTransformer
from .vector_store import VectorStore
import requests
import numpy as np

class RAGEngine:

    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.store = VectorStore()

    def chunk_text(self, docs, size=300, overlap=50):
        chunks = []
        for doc in docs:
            start = 0
            while start < len(doc):
                chunks.append(doc[start:start+size])
                start += size - overlap
        return chunks

    def build_index(self, documents):
        chunks = self.chunk_text(documents)
        embeddings = self.embedder.encode(chunks)
        self.store.save(embeddings, chunks)

    def ask(self, question):
        # ✅ if index not built, stop
        if not self.store.exists():
            return "❌ RAG index not built yet. Please build first."

        index, chunks = self.store.load()

        q_vec = self.embedder.encode([question]).astype("float32")

        # 🔥 dynamic retrieval (no fixed k)
        _, ids = index.search(q_vec, index.ntotal)

        context = "\n".join([chunks[i] for i in ids[0]])

        prompt = f"""
You are an Odoo sales assistant.
Answer ONLY from the context.

Context:
{context}

Question:
{question}
Answer:
"""
        return self.ask_llm(prompt)

    def ask_llm(self, prompt):
        res = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )
        return res.json().get("response", "⚠️ AI error")