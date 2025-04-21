from telegram import Update
from telegram.ext import ContextTypes
from database import update_config, get_config
from config import SECTIONS

async def set_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set new admin username"""
    if not context.args:
        await update.message.reply_text("Используйте: /setadmin @username")
        return
    
    new_admin = context.args[0].lstrip('@')
    update_config("admin", new_admin)
    await update.message.reply_text(f"Новый администратор: @{new_admin}")

async def set_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set link for a specific section"""
    if len(context.args) < 2:
        await update.message.reply_text("Используйте: /setlink_[раздел] [url]")
        return
    
    # Extract section from command
    command = update.message.text.split()[0]
    section = command.split('_')[1] if '_' in command else None
    
    if not section or section not in SECTIONS:
        await update.message.reply_text(
            f"Неверный раздел. Доступные разделы: {', '.join(SECTIONS.keys())}"
        )
        return
    
    url = ' '.join(context.args)
    update_config(f"link_{section}", url)
    await update.message.reply_text(f"Ссылка для раздела '{SECTIONS[section]}' обновлена!")

async def check_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Check current admin"""
    admin = get_config("admin")
    if admin:
        await update.message.reply_text(f"Текущий администратор: @{admin}")
    else:
        await update.message.reply_text("Администратор не установлен") 