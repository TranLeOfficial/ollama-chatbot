from fastapi import FastAPI
from pydantic import BaseModel  
from ollama_server import chat_with_ollama_ai

app = FastAPI()

# tạo cấu trúc contact gửi lên server có cấu trúc như sau:
class ChatRequest(BaseModel):
    message: str

# Tạo Endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "answer": f"Bạn đã nói: {request.message}"
    }

# Tạo Endpoint để chat với Ollama AI
@app.post("/chat_with_ollama")
def chat_with_ollama(request: ChatRequest):
    answer = chat_with_ollama_ai(request.message)
    return {
        "answer": answer
    }