from ollama import chat 

# Hàm chat_with_ollama_ai nhận một tin nhắn từ người dùng 
# và gửi nó đến mô hình Ollama để nhận phản hồi. 
# Nó sử dụng hàm chat từ thư viện ollama để thực hiện việc này.
def chat_with_ollama_ai(message: str):
    response = chat(
        model="qwen3:8b",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    result_message = response.message.content
    return result_message