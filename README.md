# Conversational SHL Assessment Recommender

An AI-powered conversational recommendation system that suggests relevant SHL assessments using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

## Overview

This project was built as part of the SHL AI Assessment Assignment.  
The system allows users to:

- Ask for role-specific assessments
- Receive intelligent SHL assessment recommendations
- Compare assessments
- Refine recommendations through conversational interaction
- Get grounded AI responses based on catalog evidence

The solution combines:
- FastAPI backend
- Streamlit frontend
- Gemini AI integration
- RAG-based semantic retrieval pipeline

---

# Features

- Conversational AI recommendation engine
- Retrieval-Augmented Generation (RAG)
- Semantic skill-based matching
- Clarification question handling
- Assessment comparison support
- Public API deployment
- Interactive Streamlit frontend
- Cloud-hosted backend

---

# Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM | Gemini 2.0 Flash |
| Retrieval | Custom RAG Engine |
| Data Storage | JSON Dataset |
| Deployment | Render + Streamlit Cloud |
| Language | Python |

---

# System Architecture

```text
User Query
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
RAG Retrieval Engine
    ↓
Relevant SHL Assessments Retrieved
    ↓
Gemini AI Prompt Generation
    ↓
Grounded AI Recommendation Response
