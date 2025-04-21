import os
from pathlib import Path
from dotenv import load_dotenv

# Get current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Get the absolute path to the .env file
env_path = Path(current_dir) / '.env'
print(f"Path to .env file: {env_path}")
print(f"Does .env file exist? {env_path.exists()}")

# Try to load .env file
try:
    load_dotenv(dotenv_path=env_path)
    print("\nEnvironment variables loaded successfully!")
    
    # Print all environment variables
    print("\nEnvironment variables:")
    for key, value in os.environ.items():
        if key.startswith('BOT_') or key.startswith('REFERAL_') or key.startswith('FRAMES_') or key.startswith('FONTS_') or key.startswith('GUIDES_'):
            print(f"{key}: {value[:10]}..." if value else f"{key}: None")
    
    # Verify BOT_TOKEN
    bot_token = os.getenv("BOT_TOKEN")
    if bot_token:
        print(f"\nBOT_TOKEN found: {bot_token[:10]}...")
    else:
        print("\nBOT_TOKEN not found!")
        
except Exception as e:
    print(f"\nError loading .env file: {str(e)}") 