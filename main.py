from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# گرفتن توکن و چنل از Environment Variables
TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

# دیکشنری پیام‌ها (message_id ها)
POSTS = {
    "post1": 123,
    "post2": 456,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! ربات فعاله ✅\n"
        "برای دریافت پست‌ها بنویس:\n"
        "/post1\n"
        "/post2"
    )

async def forward_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text[1:]
    message_id = POSTS.get(command)

    if message_id:
        await context.bot.forward_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=message_id
        )
        await update.message.reply_text("✅ پیام برای شما ارسال شد")
    else:
        await update.message.reply_text("❌ پست پیدا نشد")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
for key in POSTS.keys():
    app.add_handler(CommandHandler(key, forward_post))

app.run_polling()
