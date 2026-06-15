import os
import requests
from io import BytesIO
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from ai import generate_text, generate_image


# 🔐 ENV TOKEN (IMPORTANT FOR RENDER)
BOT_TOKEN = os.getenv("8236038552:AAGjXlsz5hXKTNJ6ITkuMYMFNLRqZ9l6ITw")
CHANNEL_ID = "@pumphealth"

scheduler = AsyncIOScheduler()


# 🧯 SAFE IMAGE LOADER
def safe_image(prompt):
    try:
        img_url = generate_image(prompt)
        response = requests.get(img_url, timeout=30)

        if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
            return response.content

        raise Exception("Invalid image")

    except Exception as e:
        print("Image error:", e)

        fallback = "https://picsum.photos/800/600"
        return requests.get(fallback, timeout=10).content


# 🚀 CORE POST LOGIC (shared)
async def send_post(app):
    text = generate_text()

    img_data = safe_image(
        "muscular athlete lifting weights, cinematic gym lighting, fitness motivation"
    )

    await app.bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=BytesIO(img_data),
        caption=text
    )

    print("Post sent ✔")


# 🚀 AUTO POST (scheduler safe)
async def auto_post(app):
    try:
        await send_post(app)
    except Exception as e:
        print("Auto post error:", e)


# 👋 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("AI bot is running 💪")


# 📢 MANUAL POST
async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await send_post(context.application)
        await update.message.reply_text("Post sent ✔")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


# ⚙️ INIT (Render SAFE)
async def post_init(app):
    print("Bot initialized 🚀")

    # сразу 1 пост
    await send_post(app)

    # каждые 12 часов
    scheduler.add_job(auto_post, "interval", hours=12, args=[app])
    scheduler.start()


# 🤖 APP
app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("post", post))

print("Bot running...")
app.run_polling()