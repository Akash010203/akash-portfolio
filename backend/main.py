import os
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from portfolio_context import SYSTEM_PROMPT

# Load .env from backend directory or root directory
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv()

app = FastAPI(title="Akash Portfolio AI", version="1.0.0")

# Allow your frontend (any origin during dev, restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your deployed domain in production
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY environment variable is missing. Please set it in Vercel settings or .env file."
        )
    return Groq(api_key=api_key)

# Keep a lightweight conversation memory per session using a simple in-memory store
# (resets on server restart — good enough for a portfolio)
conversation_store: dict[str, list] = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"  # frontend can pass a unique ID per visitor


@app.get("/")
async def root():
    return {"status": "Akash Portfolio AI is running ✅"}


@app.post("/api/chat")
async def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    # Get or create conversation history for this session
    history = conversation_store.setdefault(req.session_id, [])

    # Add user message to history
    history.append({"role": "user", "content": req.message.strip()})

    # Keep only last 10 turns to avoid token overflow
    if len(history) > 20:
        history = history[-20:]
        conversation_store[req.session_id] = history

    async def stream_response():
        full_reply = ""
        try:
            client = get_groq_client()
            stream = client.chat.completions.create(
                model="qwen/qwen3.8-27b",   # 27B model — fast & free on Groq
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *history
                ],
                max_tokens=512,
                temperature=0.65,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    full_reply += delta
                    yield delta

            # Save assistant reply to history after streaming completes
            history.append({"role": "assistant", "content": full_reply})
            conversation_store[req.session_id] = history

        except Exception as e:
            yield f"\n\n[Error: {str(e)}]"

    return StreamingResponse(
        stream_response(),
        media_type="text/plain; charset=utf-8",
        headers={
            "X-Accel-Buffering": "no",   # Disable Nginx buffering for streaming
            "Cache-Control": "no-cache",
        }
    )


@app.delete("/api/chat/{session_id}")
async def clear_session(session_id: str):
    """Clear conversation history for a session."""
    conversation_store.pop(session_id, None)
    return {"status": "cleared"}
