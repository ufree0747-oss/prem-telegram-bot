from datetime import date
import json

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

MY_ID =  6227990433  # replace with your real ID

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    if update.effective_user.id != MY_ID:
        return
    await update.message.reply_text("Hey Prem 👋 Your personal bot is active 24/7!")

async def log(update, context):
    if update.effective_user.id != MY_ID:
        return

    try:
        hours = float(context.args[0])
    except:
        await update.message.reply_text("Usage: /log 2.5")
        return

    today = str(date.today())
    data = load_data()
    data[today] = data.get(today, 0) + hours
    save_data(data)

    await update.message.reply_text(f"✅ Logged {hours} hours for today!")
    async def today(update, context):
    if update.effective_user.id != MY_ID:
        return

    today = str(date.today())
    data = load_data()
    hours = data.get(today, 0)

    await update.message.reply_text(f"📊 Today’s study: {hours} hours")



app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("log", log))
app.add_handler(CommandHandler("today", today))
app.run_polling()



