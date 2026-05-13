from aiogram import Bot, Dispatcher, types
import asyncio

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from services.twelvedata_service import get_realtime_price

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


# =========================
# COMMAND /harga
# =========================
@dp.message(commands=["harga"])
async def harga_handler(message: types.Message):

    price = get_realtime_price("XAU/USD")

    if price is None:
        await message.reply("Gagal ambil harga realtime.")
        return

    await message.reply(
        f"📊 XAUUSD REALTIME PRICE\n\n"
        f"Price: {price}"
    )


# helper send message biasa
async def send_message(text):
    await bot.send_message(TELEGRAM_CHAT_ID, text)


def send_telegram(text):
    asyncio.run(send_message(text))
