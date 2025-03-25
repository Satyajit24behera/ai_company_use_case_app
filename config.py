import os
from dotenv import load_dotenv

# Load environment variables from a .env file (Recommended for security)
load_dotenv()

# ✅ Store API Keys in a Dictionary
CONFIG = {
    "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY", "your_default_tavily_key"),
    "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY", "your_default_gemini_key"),
    "KAGGLE_USERNAME": os.getenv("KAGGLE_USERNAME", "your_default_kaggle_username"),
    "KAGGLE_KEY": os.getenv("KAGGLE_KEY", "your_default_kaggle_key"),
    "GITHUB_ACCESS_TOKEN": os.getenv("GITHUB_ACCESS_TOKEN", ""),  # Optional for authentication
}
