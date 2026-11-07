# ============================================================
# RAG Context — Akash Upadhyay's Portfolio AI Knowledge Base
# This is what the AI "knows" about Akash. Keep it updated!
# ============================================================

PORTFOLIO_DATA = {
    "name": "Akash Upadhyay",
    "role": "B.Tech CSE (AI & ML) student at LNCT Bhopal and freelance video editor",
    "location": "Bhopal, India",
    "availability": "Open to editing work and collaborations",
    "email": "akashupadhyay0303@gmail.com",
    "whatsapp": "+91 8463053957",
    "social": {
        "GitHub": "https://github.com/Akash010203",
        "Instagram": "https://instagram.com/akash_upadhyay03_",
        "Editing portfolio": "https://akash-edit.vercel.app/",
        "YouTube": "https://youtube.com/@veragivmg",
    },
    "tools": ["Python", "Premiere Pro", "After Effects", "Photoshop", "Illustrator", "Git", "VS Code"],
    "education": [
        "B.Tech in Computer Science Engineering (AI & ML) at LNCT Bhopal — currently in progress",
        "CS50P (Python) — completed"
    ],
    "experience": [
        {
            "title": "Freelance Video Editor",
            "details": (
                "Akash edits videos for clients, including motion graphics and caption-style edits "
                "in Premiere Pro and After Effects. Client names are kept confidential. "
                "He is skilled in storytelling through cuts, typographic animations, colour grading, and visual effects."
            )
        },
        {
            "title": "Smart India Hackathon 2026",
            "details": "Building SOVEREIGN-AI — an offline agentic AI workbench for secure, local-first industrial AI work — with a small team."
        },
        {
            "title": "Hackathon: Nebius × NVIDIA Global AI Hackathon",
            "details": "Submitted SketchForge AI, an agentic tool that converts hand-drawn sketches into full-stack web applications, in the Coding and Agentic Engineering track."
        }
    ],
    "projects": [
        {
            "id": "sketchforge",
            "title": "SketchForge AI",
            "category": "AI Tools",
            "summary": "An agentic workbench that turns hand-drawn sketches into verified, runnable web apps.",
            "description": (
                "SketchForge AI reads sketches, wireframes and whiteboard diagrams, then designs, builds, tests and repairs "
                "a full-stack web app in a closed loop. It pairs OpenCV for layout extraction with NVIDIA Nemotron models "
                "hosted on Nebius Token Factory, researches design patterns with Tavily, and validates the result in a headless "
                "Playwright browser. If the app has bugs it repairs itself — that's the agentic loop. "
                "Submitted to the Nebius × NVIDIA Global AI Hackathon (Coding and Agentic Engineering track)."
            ),
            "how_it_was_made": (
                "The pipeline has four stages: (1) Vision — OpenCV detects bounding boxes and regions in the sketch image. "
                "(2) Design — NVIDIA Nemotron (via Nebius Token Factory) interprets the layout and writes HTML/CSS/JS. "
                "(3) Research — Tavily searches for best-practice UI patterns to improve the generated code. "
                "(4) Validation — Playwright launches a headless browser, checks for JS errors and broken elements, and "
                "feeds failures back to the model for a repair cycle. The result is a working, tested web app from a napkin sketch."
            ),
            "tools": ["Python", "OpenCV", "Playwright", "Flask", "NVIDIA Nemotron", "Nebius Token Factory", "Tavily"],
            "source": "https://github.com/Akash010203/sketchforge-ai",
            "status": "Hackathon submission"
        },
        {
            "id": "veragi",
            "title": "VERAGI",
            "category": "AI Tools",
            "summary": "An AI studio that turns a client brief and raw media into a Premiere Pro / After Effects project.",
            "description": (
                "VERAGI is Akash's flagship personal project. It takes a text brief and raw footage and produces a finished "
                "editing project without manual steps. It mines tutorial videos into reusable editing 'recipes', selects the best "
                "recipe for the brief, assembles the timeline, and runs automated quality checks. The YouTube channel @veragivmg "
                "shows demos of the output."
            ),
            "how_it_was_made": (
                "VERAGI uses Phi-3.5-vision (a small multimodal model) to analyse video frames and understand visual style. "
                "ONNX Runtime runs the model locally for speed. A Python script drives the Premiere Pro API (ExtendScript/UXP) "
                "to place clips on the timeline. The quality checker compares output frames against reference thumbnails."
            ),
            "tools": ["Python", "Premiere Pro", "After Effects", "Phi-3.5-vision", "ONNX"],
            "status": "In progress"
        },
        {
            "id": "sovereign",
            "title": "SOVEREIGN-AI",
            "category": "AI Tools",
            "summary": "An offline agentic AI workbench for confidential industrial work, built for Smart India Hackathon 2026.",
            "description": (
                "SOVEREIGN-AI is a local-first workbench (SIH problem statement SIH26117) that runs open-weight LLMs with "
                "zero cloud AI calls. Everything stays on-device: the agent engine, local document search with citations, "
                "OCR for scanned documents, and generated PDF reports. Designed for sensitive industrial and government contexts "
                "where data must not leave the network."
            ),
            "how_it_was_made": (
                "Built with Python and PyTorch. llama.cpp runs Qwen3 models efficiently on CPU/GPU. A RAG pipeline indexes "
                "local documents with SQLite and sentence embeddings, so the agent can answer questions about uploaded files "
                "with citations. No internet connection needed after setup."
            ),
            "tools": ["Python", "PyTorch", "llama.cpp", "Qwen3", "SQLite"],
            "status": "In progress — Smart India Hackathon 2026 team project"
        },
        {
            "id": "portfolio",
            "title": "Video Editing Portfolio",
            "category": "Web",
            "summary": "A single-file portfolio site with a showreel, project grid and video modal.",
            "description": "A neo-brutalist portfolio for Akash's video editing work. Live at akash-edit.vercel.app.",
            "how_it_was_made": "Built with plain HTML, CSS and JavaScript — no frameworks. Deployed on Vercel from GitHub.",
            "tools": ["HTML", "CSS", "JavaScript", "Vercel"],
            "status": "Live",
            "url": "https://akash-edit.vercel.app/"
        },
        {
            "id": "readme",
            "title": "Animated GitHub Profile",
            "category": "Web",
            "summary": "A profile README with a custom banner, stats cards and a contribution animation.",
            "description": "GitHub profile at github.com/Akash010203. Features a Python-generated banner, self-hosted stats cards, and a contribution snake animation.",
            "how_it_was_made": "Python + Pillow generated the banner image. Stats cards are self-hosted on Vercel. GitHub Actions runs the snake animation on a schedule.",
            "tools": ["Python", "Pillow", "NumPy", "Vercel"],
            "status": "In progress"
        }
    ],
    "about": (
        "Akash is a B.Tech student in CSE (AI & ML) at LNCT, Bhopal, and works as a freelance video editor. "
        "Most of his projects start from a real problem he hit while editing or learning — an AI editing studio that automates "
        "routine cuts, an offline AI workbench for confidential work, and a portfolio site built from scratch. "
        "He is learning Python by building real things and prefers hands-on practice to pure theory."
    ),
    "intro": (
        "Akash studies AI and machine learning at LNCT Bhopal and edits video for clients. "
        "He builds tools that bring the two together."
    )
}

# ============================================================
# Build a compact RAG context string for the system prompt
# ============================================================
def build_rag_context() -> str:
    p = PORTFOLIO_DATA
    lines = [
        f"PERSON: {p['name']}",
        f"ROLE: {p['role']}",
        f"LOCATION: {p['location']}",
        f"AVAILABILITY: {p['availability']}",
        f"EMAIL: {p['email']}",
        f"WHATSAPP: {p['whatsapp']}",
        f"ABOUT: {p['about']}",
        "",
        "--- TOOLS & SKILLS ---",
        ", ".join(p["tools"]),
        "",
        "--- EDUCATION ---",
    ]
    for e in p["education"]:
        lines.append(f"• {e}")
    lines.append("")
    lines.append("--- EXPERIENCE ---")
    for exp in p["experience"]:
        lines.append(f"• {exp['title']}: {exp['details']}")
    lines.append("")
    lines.append("--- PROJECTS (with how they were made) ---")
    for proj in p["projects"]:
        lines.append(f"\n[{proj['title']}] ({proj['status']})")
        lines.append(f"  What: {proj['description']}")
        if "how_it_was_made" in proj:
            lines.append(f"  How it was made: {proj['how_it_was_made']}")
        lines.append(f"  Tools: {', '.join(proj['tools'])}")
        if proj.get("url"):
            lines.append(f"  Live URL: {proj['url']}")
        if proj.get("source"):
            lines.append(f"  Source code: {proj['source']}")
    lines.append("")
    lines.append("--- SOCIAL LINKS ---")
    for label, url in p["social"].items():
        lines.append(f"  {label}: {url}")
    return "\n".join(lines)


SYSTEM_PROMPT = f"""
You are an AI assistant embedded in Akash Upadhyay's personal portfolio website.
Your purpose: help visitors — recruiters, clients, collaborators — learn about Akash in a friendly, concise, helpful way.

RULES:
1. Answer only about Akash, his work, skills, projects, and how to contact him.
2. If a visitor asks how a specific project or video was made, explain it clearly using the "how_it_was_made" details below.
3. Keep answers short (2–5 sentences) unless the visitor asks for a deep technical explanation.
4. Always be warm and professional. Use "Akash" (not "I") — you are the assistant, not Akash.
5. If asked something you genuinely don't know, say so and invite them to contact Akash directly at {PORTFOLIO_DATA['email']}.
6. For collaborations or editing work, direct visitors to: Email — {PORTFOLIO_DATA['email']} or WhatsApp — {PORTFOLIO_DATA['whatsapp']}.
7. Never make up facts. Only use the context provided below.

=== PORTFOLIO KNOWLEDGE BASE (RAG Context) ===
{build_rag_context()}
=== END OF KNOWLEDGE BASE ===
"""
