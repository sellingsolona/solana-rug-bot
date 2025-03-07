from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message with menu buttons"""
    keyboard = [
        [InlineKeyboardButton("🌐 Dashboard", callback_data='dashboard')],
        [InlineKeyboardButton("🔥 Features", callback_data='features')],
        [InlineKeyboardButton("🛒 Purchase & Pricing", callback_data='pricing')],
        [InlineKeyboardButton("ℹ️ More Info", callback_data='info')],
        [InlineKeyboardButton("✅ Vouches", url="https://t.me/vouchesrugbot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to SolCoin Rug Bot!

"
        "User ID: Guest
"
        "Date & Time: (Auto-Generated)
"
        "Current Plan: None

"
        "For help, contact @Rugbothelp",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles button clicks"""
    query = update.callback_query
    await query.answer()

    if query.data == "dashboard":
        text = "🌐 Dashboard - Select an option:"
    elif query.data == "features":
        text = "🔥 Features: Auto Volume, Human Mode, Micro Buy, Sell All..."
    elif query.data == "pricing":
        text = "🛒 Purchase Options: Lifetime License (3 SOL), 10-Day Trial (0.5 SOL)."
    elif query.data == "info":
        text = "ℹ️ How does RugsolAI work? It lets you launch memecoins with built-in tools."
    else:
        text = "Welcome back! Select an option:"

    await query.edit_message_text(text=text)
