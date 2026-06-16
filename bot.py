import os
import asyncio
import requests
from io import BytesIO
from telegram import Bot
from ai import generate_text, generate_image_url

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@pumphealth"  # Change if needed

async def main():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN is missing! Check GitHub Secrets.")

    bot = Bot(token=BOT_TOKEN)

    text = generate_text()
    image_url = generate_image_url()

    print("Generated text:", text[:100] + "..." if len(text) > 100 else text)
    print("Image URL:", image_url)

    try:
        response = requests.get(image_url, timeout=60)
        response.raise_for_status()

        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=BytesIO(response.content),
            caption=text,
            parse_mode="Markdown"  # Enables bold, etc.
        )
        print("✅ Post published successfully!")
    except Exception as e:
        print("❌ Error sending post:", e)


if __name__ == "__main__":
    asyncio.run(main())