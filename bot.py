import os
import json
from datetime import date
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ===================== CONFIG =====================
TOKEN = os.getenv("TOKEN")          # Bot token from Render env
MY_ID =  6227990433                   # 🔴 REPLACE with your Telegram user ID
DATA_FILE = "data.json"
# =================================================

# ---------- Data helpers ----------
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# ---------- Commands ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_ID:
        return
    await update.message.reply_text(
        "Hey Prem 👋 Your personal bot is active 24/7!\n\n"
        "Commands:\n"
        "/log <hours>  ➜ Log study time\n"
        "/today        ➜ See today’s total"
    )

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_ID:
        return

    if not context.args:
        await update.message.reply_text("Usage: /log 2.5")
        return

    try:
        hours = float(context.args[0])
    except:
        await update.message.reply_text("Please enter a number.\nExample: /log 1.5")
        return

    today = str(date.today())
    data = load_data()
    data[today] = data.get(today, 0) + hours
    save_data(data)

    await update.message.reply_text(f"✅ Logged {hours} hours for today!")

async def today_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != MY_ID:
        return

    today = str(date.today())
    data = load_data()
    hours = data.get(today, 0)

    await update.message.reply_text(f"📊 Today’s study: {hours} hours")

# ---------- App setup ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("log", log))
app.add_handler(CommandHandler("today", today_cmd))

app.run_polling()
