# CapLibrarySSS Telegram Bot

Telegram bot for managing and sharing various resources through dynamic links.

## Features

- Interactive menu with 4 sections (Рефералки, Рамки, Шрифты, Гайды)
- Dynamic link management through admin commands
- PostgreSQL database for configuration storage
- Support for preview images through CDN
- Asynchronous architecture

## Setup

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your configuration:
   ```bash
   cp .env.example .env
   ```
5. Set up PostgreSQL database and update DATABASE_URL in `.env`
6. Run the bot:
   ```bash
   python main.py
   ```

## Admin Commands

- `/setadmin @username` - Set new admin
- `/checkadmin` - Check current admin
- `/setlink_referal [url]` - Set link for Рефералки section
- `/setlink_frames [url]` - Set link for Рамки section
- `/setlink_fonts [url]` - Set link for Шрифты section
- `/setlink_guides [url]` - Set link for Гайды section

## Deployment

The bot can be deployed on Railway.app:

1. Create a new Railway project
2. Connect your GitHub repository
3. Add environment variables from `.env`
4. Deploy the application

## License

MIT 