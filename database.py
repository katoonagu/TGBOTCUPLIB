import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

def init_db():
    """Initialize database and create necessary tables"""
    try:
        conn = sqlite3.connect('caplibrary.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS config (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        conn.commit()
        print("✅ База данных подключена!")
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        raise  # Пробрасываем ошибку дальше для обработки в main.py
    finally:
        if 'conn' in locals():
            conn.close()

def update_config(key: str, value: str):
    """Update or insert configuration value"""
    conn = None
    try:
        conn = sqlite3.connect('caplibrary.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO config (key, value) 
            VALUES (?, ?)
        ''', (key, value))
        conn.commit()
    except Exception as e:
        print(f"❌ Ошибка обновления конфига: {e}")
        raise
    finally:
        if conn:
            conn.close()

def get_config(key: str) -> str:
    """Get configuration value"""
    conn = None
    try:
        conn = sqlite3.connect('caplibrary.db')
        cursor = conn.cursor()
        cursor.execute('SELECT value FROM config WHERE key = ?', (key,))
        result = cursor.fetchone()
        return result[0] if result else ""
    except Exception as e:
        print(f"❌ Ошибка получения конфига: {e}")
        return ""
    finally:
        if conn:
            conn.close() 