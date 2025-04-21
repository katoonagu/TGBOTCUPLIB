import os
import asyncio
import logging
import time
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram.error import NetworkError
from telegram import Update
from config import BOT_TOKEN
from database import init_db
from handlers import user_commands, admin_commands

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def error_handler(update, context):
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    # Initialize database
    init_db()
    
    # Create application with token verification
    if not BOT_TOKEN:
        raise ValueError("Bot token is not set!")
    
    print(f"Starting bot with token: {BOT_TOKEN[:10]}...")
    
    # Create application with custom settings
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .read_timeout(30)  # Increase read timeout
        .write_timeout(30)  # Increase write timeout
        .connect_timeout(30)  # Increase connect timeout
        .build()
    )
    
    # Register handlers
    application.add_handler(CommandHandler("start", user_commands.start))
    application.add_handler(CommandHandler("setadmin", admin_commands.set_admin))
    application.add_handler(CommandHandler("checkadmin", admin_commands.check_admin))
    application.add_handler(CommandHandler("setlink_referal", admin_commands.set_link))
    application.add_handler(CommandHandler("setlink_frames", admin_commands.set_link))
    application.add_handler(CommandHandler("setlink_fonts", admin_commands.set_link))
    application.add_handler(CommandHandler("setlink_guides", admin_commands.set_link))
    application.add_handler(CallbackQueryHandler(user_commands.handle_buttons))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start the bot with retry logic
    print("Bot is starting...")
    while True:
        try:
            application.run_polling(
                allowed_updates=Update.ALL_TYPES,
                drop_pending_updates=True
            )
        except NetworkError as e:
            logger.error(f"Network error occurred: {e}")
            print("Network error occurred. Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            print("Unexpected error occurred. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    main() 