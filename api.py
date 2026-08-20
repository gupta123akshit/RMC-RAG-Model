from fastapi import FastAPI
from pydantic import BaseModel

from src.rag import answer_question


app = FastAPI(
    title="RMC RAG API",
    description="RAG system for RMC mix-design documents",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RMC RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):

    answer, results = answer_question(
        query=request.question,
        top_k=3
    )

    sources = []

    seen = set()

    for metadata in results["metadatas"][0]:

        source_key = (
            metadata["source"],
            metadata["page"]
        )

        if source_key not in seen:

            sources.append({
                "source": metadata["source"],
                "page": metadata["page"]
            })

            seen.add(source_key)

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }