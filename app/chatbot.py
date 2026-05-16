import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class SHLChatbot:
    def __init__(self, rag):
        self.rag = rag
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, query):
        retrieved = self.rag.retrieve(query)

        context = "\n".join([
            f"{r['name']} - {r['description']}"
            for r in retrieved
        ])

        prompt = f"""
        User Query:
        {query}

        Relevant Assessments:
        {context}

        Recommend the best assessments and explain why.
        """

        try:
            response = self.model.generate_content(prompt)
            ai_response = response.text

        except Exception:
            ai_response = "AI service temporarily unavailable."

        return {
            "response": ai_response,
            "recommendations": retrieved
        }