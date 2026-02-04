from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qusai_core.pipeline.middleware import QusaiMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_TOKEN = os.environ.get("HF_TOKEN")
middleware = None

@app.on_event("startup")
async def startup():
    global middleware
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN not set!")
    middleware = QusaiMiddleware(
        model_id="Qwen/Qwen2.5-72B-Instruct",
        api_token=HF_TOKEN,
        lazy_load=False
    )

class ChatRequest(BaseModel):
    message: str
    arabic: bool = False

@app.get("/")
def root():
    return {"status": "QUSAI API Running", "model": "Qwen 72B"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        query = req.message
        if req.arabic:
            query += " (Answer in Arabic only)"
        response = middleware.process_query(query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
