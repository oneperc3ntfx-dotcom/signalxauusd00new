from aiogram import Bot
import asyncio

from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)

bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def send_message(message):

    await bot.send_message(
        TELEGRAM_CHAT_ID,
        message
    )


def send_telegram(message):

    asyncio.run(
        send_message(message)
    )
