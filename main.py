from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

POSTS = {
    "post1": 10,
    "post2": 25,
    "post3": 40,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("لینک نامعتبر است.")
        return

    code = context.args[0]

    if code not in POSTS:
        await update.message.reply_text("پست مورد نظر پیدا نشد.")
        return

    message_id = POSTS[code]

    await context.bot.forward_message(
        chat_id=update.effective_chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=message_id
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
