import os

from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = os.getenv("OPENAI_URL")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
