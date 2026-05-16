from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class SHLChatbot:

    def __init__(self, rag_engine):
        self.rag = rag_engine

    def generate_response(self, user_query):

        retrieved = self.rag.search(user_query)

        context = "\n\n".join([
            f"""
Name: {r['name']}
Category: {r['category']}
Skills: {', '.join(r['skills'])}
Description: {r['description']}
"""
            for r in retrieved
        ])

        prompt = f"""
You are an SHL assessment recommendation assistant.

User Query:
{user_query}

Relevant Assessments:
{context}

Tasks:
1. Recommend the best assessments
2. Explain why they fit
3. Keep response concise
4. Ask one follow-up clarifying question
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return {
                "recommendations": retrieved,
                "response": response.text
            }

        except Exception as e:

            return {
                "recommendations": retrieved,
                "response": f"Error generating response: {str(e)}"
            }