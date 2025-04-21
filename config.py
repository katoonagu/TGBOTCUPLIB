import os
from pathlib import Path
from dotenv import load_dotenv

# Get current working directory and load .env file
current_dir = os.getcwd()
env_path = Path(current_dir) / '.env'
load_dotenv(dotenv_path=env_path)

# Debug: Print all environment variables
print("Environment variables:")
for key, value in os.environ.items():
    if key.startswith('BOT_') or key.startswith('REFERAL_') or key.startswith('FRAMES_') or key.startswith('FONTS_') or key.startswith('GUIDES_'):
        print(f"{key}: {value[:10]}..." if value else f"{key}: None")

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables!")
print(f"Bot token loaded: {BOT_TOKEN[:10]}...")  # Print first 10 chars for security

DATABASE_URL = os.getenv("DATABASE_URL")

# Menu sections
SECTIONS = {
    "referal": "🤑 Рефералки",
    "frames": "🎥 Рамки",
    "fonts": "🔤 Шрифты",
    "guides": "📚 Гайды"
}

# Image URLs
IMAGE_URLS = {
    "referal": os.getenv("REFERAL_IMG_URL"),
    "frames": os.getenv("FRAMES_IMG_URL"),
    "fonts": os.getenv("FONTS_IMG_URL"),
    "guides": os.getenv("GUIDES_IMG_URL")
}

# Verify all required environment variables are set
required_vars = ["BOT_TOKEN", "REFERAL_IMG_URL", "FRAMES_IMG_URL", "FONTS_IMG_URL", "GUIDES_IMG_URL"]
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# CDN configuration
CDN_BASE_URL = os.getenv("CDN_BASE_URL", "https://your-cdn.com") 