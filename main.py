import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.jobs import run_analysis
from services.telegram_service import bot, dp
from services.price_cache import update_price

from pytz import utc

scheduler = AsyncIOScheduler(timezone=utc)


# =========================
# ANALYSIS TIAP JAM 00
# =========================
scheduler.add_job(run_analysis, "cron", minute=0)


# =========================
# BACKGROUND PRICE UPDATE
# =========================
async def price_loop():

    while True:
        update_price()
        await asyncio.sleep(5)


async def main():

    print("BOT RUNNING...")

    scheduler.start()

    # start cache updater
    asyncio.create_task(price_loop())

    # telegram polling (/harga)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
