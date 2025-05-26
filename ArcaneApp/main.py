from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from vector_store import VectorStore
from rag_engine import build_vector_store, answer_question
from local_llm import ask_local_llm

load_dotenv()
API_KEY = os.getenv("API_SECRET_KEY")

app = FastAPI()
store = VectorStore(dim=768)  # Assuming 768 is the embedding dimension
store.load()  # Load the vector store if it exists

class AskRequest(BaseModel):
    question: str
    api_key: str


@app.post("/ask")
def ask(request: AskRequest):
    if request.api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
    
    context = answer_question(request.question, store)

    prompt = f"""You are a helpful assistant. Answer the question using ONLY the context provided below. If the answer is not present, say "I don't know."

Context:
{context}

Question: {request.question}
"""
    
    answer = ask_local_llm(prompt)
    return {"answer": answer}