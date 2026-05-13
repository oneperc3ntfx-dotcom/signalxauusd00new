from aiogram import Bot, Dispatcher, types
import asyncio

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from services.price_cache import get_cached_price

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


# =========================
# /harga COMMAND
# =========================
@dp.message(lambda message: message.text == "/harga")
async def harga_handler(message: types.Message):

    price = get_cached_price()

    if price is None:
        await message.reply("⚠️ No realtime price")
        return

    await message.reply(f"📈 XAUUSD : {price}")


# =========================
# SEND MESSAGE
# =========================
async def send_message(text):
    await bot.send_message(TELEGRAM_CHAT_ID, text)


def send_telegram(text):
    asyncio.run(send_message(text))
