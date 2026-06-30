from ollama import chat

print("=== AI Chatbot ===")
print("Gõ 'exit' để thoát.\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = chat(
        model="qwen3:8b",
        messages=messages
    )

    ai_message = response.message.content

    print(f"\nAI: {ai_message}\n")

    messages.append({
        "role": "assistant",
        "content": ai_message
    })