import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class SHLRAG:
    def __init__(self, json_path):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        self.documents = []

        for item in self.data:
            text = f"""
            Assessment: {item['name']}
            Category: {item['category']}
            Skills: {', '.join(item['skills'])}
            Description: {item['description']}
            Roles: {', '.join(item['job_roles'])}
            """
            self.documents.append(text)

        embeddings = self.model.encode(self.documents)

        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings, dtype=np.float32))

        self.embeddings = embeddings

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])

        distances, indices = self.index.search(
            np.array(query_embedding, dtype=np.float32),
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.data[idx])

        return results