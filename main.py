from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI()

# tạo cấu trúc contact gửi lên server có cấu trúc như sau:
class ChatRequest(BaseModel):
    massage: str

# Tạo Endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "answer": f"Bạn đã nói: {request.massage}"
    }