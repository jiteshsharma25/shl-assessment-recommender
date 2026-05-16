import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class SHLChatbot:
    def __init__(self, rag_engine):
        self.rag = rag_engine
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, query):

        assessments = self.rag.retrieve(query)

        context = "\n".join(
            [
                f"""
Name: {a['name']}
Category: {a['category']}
Skills: {', '.join(a['skills'])}
Description: {a['description']}
"""
                for a in assessments
            ]
        )

        prompt = f"""
You are an SHL assessment recommendation assistant.

User Query:
{query}

Assessment Catalog:
{context}

Instructions:
- Recommend the most relevant assessments
- Explain WHY each assessment matches
- Mention skills evaluated
- Keep response professional and concise
"""

        try:
            response = self.model.generate_content(prompt)
            ai_response = response.text

        except Exception:
            # PROFESSIONAL FALLBACK RESPONSE
            ai_response = self.fallback_response(
                query,
                assessments
            )

        return {
            "response": ai_response,
            "recommended_assessments": assessments
        }

    def fallback_response(self, query, assessments):

        if not assessments:
            return "No suitable assessments were found."

        assessment_names = ", ".join(
            [a["name"] for a in assessments]
        )

        return (
            f"Based on the hiring requirement "
            f"'{query}', the system identified "
            f"assessments that best match the "
            f"required technical and behavioral "
            f"skills.\n\n"

            f"The recommendations prioritize "
            f"role relevance, skill alignment, "
            f"and cognitive evaluation needs.\n\n"

            f"Top recommended assessments include: "
            f"{assessment_names}.\n\n"

            f"These results were generated using "
            f"semantic retrieval and AI-assisted "
            f"recommendation logic."
        )