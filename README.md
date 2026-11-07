# Akash Upadhyay — Portfolio with AI Assistant 🚀

A modern, neo-brutalist developer & video editor portfolio featuring an interactive **AI Assistant** grounded in portfolio data via RAG (Retrieval-Augmented Generation).

---

## ✨ Features

- **Personal Portfolio**: Showcases projects (SketchForge AI, VERAGI, SOVEREIGN-AI), editing work, experience, and contact links.
- **Embedded AI Chatbot**: Visitors can ask questions about Akash, his technical stack, and how specific projects were built.
- **Real-time Streaming**: Powered by Server-Sent Events (SSE) for a responsive typewriter effect.
- **Fast & Free LLM Inference**: Runs on [Groq Cloud](https://groq.com) using open-weights models (`qwen/qwen3.8-27b`).
- **Secure Backend**: FastAPI serves as the proxy; API keys are never exposed to the client.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (Neo-brutalist design, motion physics, custom cursors), Vanilla JavaScript
- **Backend**: Python 3.10+, [FastAPI](https://fastapi.tiangolo.com/), Uvicorn
- **AI / LLM**: [Groq Cloud](https://console.groq.com) (`qwen/qwen3.8-27b`)
- **Knowledge Base**: Context grounding with structured portfolio knowledge

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Akash010203/new-ai-portfoli.git
cd new-ai-portfoli
```

### 2. Set up the FastAPI Backend
```bash
cd backend

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Add your Groq API Key
1. Get a free API key at [console.groq.com/keys](https://console.groq.com/keys).
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Open `.env` and set:
   ```env
   GROQ_API_KEY=gsk_your_actual_key_here
   ```

### 4. Run the Backend Server
```bash
uvicorn main:app --reload
```
The backend will run on `http://127.0.0.1:8000`.

### 5. Launch the Frontend
Simply open `index.html` in your browser, or use VS Code's Live Server extension. Click the floating chat button in the bottom right corner to chat with the AI!

---

## 📬 Contact
- **Email**: akashupadhyay0303@gmail.com
- **WhatsApp**: +91 8463053957
- **GitHub**: [@Akash010203](https://github.com/Akash010203)
