import asyncio

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from config import BOT_TOKEN
from data_feed import stream_price, get_last_price


# =========================
# /PRICE COMMAND
# =========================
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    price = get_last_price()

    if price is None:
        await update.message.reply_text("⚠️ No realtime price")
        return

    await update.message.reply_text(f"📈 XAUUSD : {price}")


# =========================
# SIMPLE SIGNAL TEST
# =========================
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    price = get_last_price()

    if price is None:
        return await update.message.reply_text("⚠️ No price")

    bias = "BUY" if int(price) % 2 == 0 else "SELL"

    await update.message.reply_text(
        f"📊 SIGNAL: {bias}\n📈 PRICE: {price}"
    )


# =========================
# BACKGROUND STREAM START
# =========================
async def post_init(app):

    lock = asyncio.Lock()

    asyncio.create_task(stream_price(lock))

    print("BOT RUNNING...")


# =========================
# MAIN
# =========================
def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("signal", signal))

    app.post_init = post_init

    app.run_polling()


if __name__ == "__main__":
    main()
