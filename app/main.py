from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_engine import SHLRAG
from app.chatbot import SHLChatbot

app = FastAPI(title="SHL Assessment Recommender")

rag = SHLRAG("app/data/assessments.json")
chatbot = SHLChatbot(rag)


class UserQuery(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "SHL AI Assessment Recommender API Running"
    }


@app.post("/recommend")
def recommend_assessment(user_query: UserQuery):
    result = chatbot.generate_response(user_query.query)
    return result