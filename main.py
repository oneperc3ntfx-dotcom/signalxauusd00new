import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.jobs import run_analysis
from services.telegram_service import bot, dp
from services.price_cache import update_price

from pytz import utc

scheduler = AsyncIOScheduler(timezone=utc)


# =========================
# SIGNAL TIAP JAM 00
# =========================
scheduler.add_job(run_analysis, "cron", minute=0)


# =========================
# PRICE LOOP (CACHE UPDATE)
# =========================
async def price_loop():

    while True:
        try:
            update_price()
        except Exception as e:
            print("Price loop error:", e)

        await asyncio.sleep(5)


async def main():

    print("BOT RUNNING...")

    scheduler.start()

    asyncio.create_task(price_loop())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
