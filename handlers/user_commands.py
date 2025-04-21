from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import ContextTypes
from telegram.error import BadRequest
from config import SECTIONS, IMAGE_URLS
from database import get_config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with menu buttons"""
    keyboard = [
        [InlineKeyboardButton(text, callback_data=key)]
        for key, text in SECTIONS.items()
    ]
    
    await update.message.reply_text(
        "Добро пожаловать в CapLibrarySSS! Выберите раздел:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    section = query.data
    if section not in SECTIONS:
        return
    
    try:
        # Get section data from database
        link = get_config(f"link_{section}")
        admin = get_config("admin")
        
        # Create response message
        message = f"*{SECTIONS[section]}*\n\n"
        if admin:
            message += f"Администратор: @{admin}\n\n"
        if link:
            message += f"[Перейти к разделу]({link})"
        
        # Create keyboard with link button if available
        keyboard = []
        if link:
            keyboard.append([InlineKeyboardButton("Перейти", url=link)])
        
        # Get image URL from config
        image_url = IMAGE_URLS.get(section)
        
        # Send or update message
        if image_url:
            try:
                await update.callback_query.message.edit_media(
                    media=InputMediaPhoto(
                        media=image_url,
                        caption=message,
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None
                )
            except BadRequest:
                await query.message.reply_text("❌ Ошибка загрузки картинки. Проверьте ссылку!")
                await query.message.edit_text(
                    text=message,
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None
                )
        else:
            await query.message.edit_text(
                text=message,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None
            )
    except Exception as e:
        await query.message.reply_text(f"❌ Произошла ошибка: {str(e)}") 