# 📄 AI PDF Chatbot (Local Llama3 + Ollama)

A fully local **Retrieval-Augmented Generation (RAG)** chatbot that allows users to interact with PDF documents using **Llama3 running locally via Ollama**.

This project demonstrates real-world implementation of:
- Vector databases  
- Local LLM deployment  
- Semantic search  
- Privacy-first AI systems  

🔒 100% private — no external APIs  
⚡ Fast semantic search using FAISS  
🤖 Local LLM powered by Llama3  
💾 Export conversation as TXT  

---

## 📸 Application Preview

> 📌 Create a folder called `screenshots/` in your GitHub repository and place images inside it.

Add screenshots below this section:

### 💬 Chat Interface
![Chat UI](screenshots/chat-ui.png)

### 📂 PDF Upload & Processing
![Upload](screenshots/upload.png)

### 📚 Context-Aware Answers
![Answer](screenshots/answer.png)

### 💾 Conversation Export
![Export](screenshots/export.png)

---

## 🚀 Features

- 📂 Upload multiple PDF documents  
- 🔍 Semantic search using vector embeddings  
- 🤖 Chat with documents using Llama3 (local)  
- 🧠 Conversation memory  
- 💬 Modern chat interface  
- 💾 Download conversation as TXT  
- 🔒 Fully offline and privacy-focused  
- 🖥 Optional GPU acceleration  
- ⚡ Fast FAISS vector indexing  

---

## 🏗 Tech Stack

- **Frontend:** Streamlit  
- **LLM Runtime:** Ollama  
- **Model:** Llama3  
- **Embeddings:** Sentence Transformers (MiniLM)  
- **Vector Database:** FAISS  
- **Framework:** LangChain  
- **Language:** Python  

---

## 🧠 How It Works

1. PDF files are uploaded and text is extracted.  
2. The text is split into smaller chunks.  
3. Chunks are converted into embeddings.  
4. FAISS stores embeddings for fast semantic search.  
5. Llama3 retrieves relevant chunks and generates answers.  
6. Chat history is stored in memory.  
7. Users can export the full conversation as a `.txt` file.  

This architecture follows the **Retrieval-Augmented Generation (RAG)** pattern.

---

## 💾 Conversation Export

Users can download the entire chat conversation in **TXT format** for:
- Research documentation  
- Compliance tracking  
- Knowledge sharing  
- Meeting summaries  

---

## 🔐 Privacy & Security

This application:
- Runs completely locally  
- Does not send data to external APIs  
- Stores embeddings locally using FAISS  
- Uses Ollama for offline LLM inference  

Your documents never leave your system.

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-pdf-chatbot.git
cd ai-pdf-chatbot
