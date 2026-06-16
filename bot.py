import os
import asyncio
import requests

from io import BytesIO
from telegram import Bot

from ai import generate_text, generate_image


BOT_TOKEN = os.getenv("8236038552:AAHAd_zsplGXAOViCe5glC96BIDE3lDG5Ok")
CHANNEL_ID = "@pumphealth"


async def main():

    bot = Bot(BOT_TOKEN)

    text = generate_text()

    image_url = generate_image()

    response = requests.get(image_url, timeout=60)

    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=BytesIO(response.content),
        caption=text
    )

    print("Post published successfully!")


if __name__ == "__main__":
    asyncio.run(main())