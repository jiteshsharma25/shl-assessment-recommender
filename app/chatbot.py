import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class SHLChatbot:
    def __init__(self, rag_engine):
        self.rag = rag_engine
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, query):

        assessments = self.rag.retrieve(query)

        context = "\n".join([
            f"""
            Name: {a['name']}
            Category: {a['category']}
            Skills: {', '.join(a['skills'])}
            Description: {a['description']}
            """
            for a in assessments
        ])

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
            ai_response = self.generate_fallback_response(
                query,
                assessments
            )

        return {
            "response": ai_response,
            "recommended_assessments": assessments
        }

    def generate_fallback_response(self, query, assessments):

        if not assessments:
            return (
                "I could not find suitable assessments "
                "for the provided query."
            )

        response = (
            f"For the query '{query}', "
            f"I recommend the following assessments:\n\n"
        )

        for a in assessments:
            response += (
                f"• {a['name']} ({a['category']})\n"
                f"  Skills: {', '.join(a['skills'])}\n"
                f"  Why: {a['description']}\n\n"
            )

        response += (
            "These recommendations were selected "
            "using semantic similarity retrieval "
            "and skill matching."
        )

        return response