# Ollama Chatbot

A simple AI chatbot built with Python and Ollama using the **Qwen3:8B** language model. The chatbot runs locally on your machine without requiring any cloud API.

---

## Features

- Chat with a local LLM
- Runs completely offline
- Simple terminal interface
- Streaming AI response
- Powered by Qwen3:8B

---

## Tech Stack

- Python 3
- Ollama
- Qwen3:8B

---

## Prerequisites

### 1. Install Python

Download Python:

https://www.python.org/downloads/

Verify installation:

```bash
python3 --version
```

---

### 2. Install Ollama

macOS

```bash
brew install ollama
```

Or download directly from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

### 3. Download the Qwen3:8B Model

Download the model:

```bash
ollama pull qwen3:8b
```

Verify the model is installed:

```bash
ollama list
```

You should see:

```bash
qwen3:8b
```

---

## Clone Project

```bash
git clone https://github.com/<your-username>/ollama-chatbot.git
```

Move into the project folder:

```bash
cd ollama-chatbot
```

---

## Create Virtual Environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama

If Ollama is not running, start the server:

```bash
ollama serve
```

---

## Run Chatbot

```bash
python ollama_client.py
```

---

## Example

```text
You : Hello
AI  : Hi! How can I help you today?
```

---

## Project Structure

```text
ollama-chatbot/
│
├── ollama_client.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Useful Ollama Commands

List installed models:

```bash
ollama list
```

Run Qwen3:8B directly:

```bash
ollama run qwen3:8b
```

Download the model:

```bash
ollama pull qwen3:8b
```

Remove the model:

```bash
ollama rm qwen3:8b
```

View model information:

```bash
ollama show qwen3:8b
```

---

## Future Improvements

- Chat memory
- FastAPI backend
- Web interface
- RAG with PDF documents
- Docker deployment
- Multi-model support