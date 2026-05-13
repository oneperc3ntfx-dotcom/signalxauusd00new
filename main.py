import asyncio
import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from config import BOT_TOKEN, CHAT_ID
from data_feed import last_price, stream_price

logging.basicConfig(level=logging.INFO)


# ================= PRICE COMMAND =================
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not last_price:
        return await update.message.reply_text("⚠️ No realtime price")

    await update.message.reply_text(f"📈 XAUUSD : {last_price}")


# ================= SIMPLE SIGNAL =================
def smc_signal(price):

    if int(price) % 2 == 0:
        return "BUY"
    return "SELL"


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not last_price:
        return await update.message.reply_text("⚠️ No price")

    bias = smc_signal(last_price)

    await update.message.reply_text(
        f"📊 SIGNAL: {bias}\n📈 PRICE: {last_price}"
    )


# ================= BACKGROUND TASK =================
async def post_init(app):

    lock = asyncio.Lock()

    asyncio.create_task(stream_price(lock))

    print("BOT RUNNING...")


# ================= MAIN =================
def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("signal", signal))

    app.post_init = post_init

    app.run_polling()


if __name__ == "__main__":
    main()
