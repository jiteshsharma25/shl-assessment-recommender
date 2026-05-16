import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SHLRAG:
    def __init__(self, json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            self.assessments = json.load(f)

        self.documents = [
            f"{a['name']} {a['category']} {' '.join(a['skills'])} {a['description']}"
            for a in self.assessments
        ]

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)

    def retrieve(self, query, top_k=3):
        query_vector = self.vectorizer.transform([query])

        similarities = cosine_similarity(
            query_vector,
            self.doc_vectors
        ).flatten()

        top_indices = similarities.argsort()[-top_k:][::-1]

        return [self.assessments[i] for i in top_indices]