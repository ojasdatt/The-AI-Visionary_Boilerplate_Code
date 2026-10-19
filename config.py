import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
# Override this in .env when switching to another Groq vision model.
GROQ_VISION_MODEL = (
    os.getenv("GROQ_VISION_MODEL", "").strip() or "qwen/qwen3.8-27b"
)
