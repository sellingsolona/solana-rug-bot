import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers import start, button

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def main():
    """Start the bot"""
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command and button handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
