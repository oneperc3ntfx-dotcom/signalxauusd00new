from aiogram import Bot, Dispatcher, types
import asyncio

from config import BOT_TOKEN, CHAT_ID
from services.finnhub_service import get_realtime_price

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# =========================
# /harga COMMAND
# =========================
@dp.message(lambda message: message.text == "/harga")
async def harga_handler(message: types.Message):

    price = get_realtime_price()

    if price is None:
        await message.reply("⚠️ No realtime price")
        return

    await message.reply(f"📊 XAUUSD : {price}")


# =========================
# SEND MESSAGE
# =========================
async def send_message(text):
    await bot.send_message(CHAT_ID, text)


def send_telegram(text):
    asyncio.run(send_message(text))
