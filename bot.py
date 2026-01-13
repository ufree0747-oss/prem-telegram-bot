import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

MY_ID =  6227990433  # replace with your real ID

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    if update.effective_user.id != MY_ID:
        return
    await update.message.reply_text("Hey Prem 👋 Your personal bot is active 24/7!")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()


