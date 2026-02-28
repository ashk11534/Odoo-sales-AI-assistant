import faiss
import os
import pickle
import numpy as np

BASE_PATH = "D:/odoo_rag_data"
INDEX_FILE = os.path.join(BASE_PATH, "sales.index")
META_FILE = os.path.join(BASE_PATH, "chunks.pkl")

class VectorStore:

    def __init__(self):
        os.makedirs(BASE_PATH, exist_ok=True)

    def save(self, embeddings, chunks):
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings.astype("float32"))

        faiss.write_index(index, INDEX_FILE)

        with open(META_FILE, "wb") as f:
            pickle.dump(chunks, f)

    def exists(self):
        return os.path.exists(INDEX_FILE) and os.path.exists(META_FILE)

    def load(self):
        index = faiss.read_index(INDEX_FILE)
        with open(META_FILE, "rb") as f:
            chunks = pickle.load(f)
        return index, chunks