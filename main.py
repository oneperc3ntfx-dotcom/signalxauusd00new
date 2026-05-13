import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import BOT_TOKEN
from data_feed import stream_price, get_last_price
from scheduler import hourly_scheduler, pro_max_scheduler


# ================= COMMAND PRICE =================
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    price = get_last_price()

    if price is None:
        await update.message.reply_text("⚠️ No realtime price")
        return

    await update.message.reply_text(f"📈 XAUUSD : {price}")


# ================= COMMAND START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("🤖 XAUUSD BOT ACTIVE")


# ================= INIT =================
async def post_init(app):

    lock = asyncio.Lock()

    asyncio.create_task(stream_price(lock))

    asyncio.create_task(hourly_scheduler(app))
    # asyncio.create_task(pro_max_scheduler(app))  # optional mode

    print("BOT RUNNING...")


# ================= MAIN =================
def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    app.post_init = post_init

    app.run_polling()


if __name__ == "__main__":
    main()
