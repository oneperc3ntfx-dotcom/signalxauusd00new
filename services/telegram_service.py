from aiogram import Bot, Dispatcher, types
import asyncio

from config import BOT_TOKEN, CHAT_ID
from services.price_cache import get_cached_price

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN belum di-set di Railway")

bot = Bot(token=str(BOT_TOKEN))
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

    await message.reply(f"📊 XAUUSD : {price}")


# =========================
# SEND MESSAGE
# =========================
async def send_message(text):
    if not CHAT_ID:
        return

    await bot.send_message(CHAT_ID, text)


def send_telegram(text):
    asyncio.run(send_message(text))
