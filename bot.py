import os
import asyncio
import requests

from io import BytesIO
from telegram import Bot

from ai import generate_text, generate_image


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@pumphealth"


async def main():

    # ❗ защита от пустого токена
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing (check GitHub Secrets)")

    bot = Bot(token=BOT_TOKEN)

    text = generate_text()

    # ❗ FIX: generate_image требует prompt
    image_url = generate_image("muscular athlete gym motivation, cinematic lighting")

    response = requests.get(image_url, timeout=60)
    response.raise_for_status()

    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=BytesIO(response.content),
        caption=text
    )

    print("Post published successfully!")


if __name__ == "__main__":
    asyncio.run(main())