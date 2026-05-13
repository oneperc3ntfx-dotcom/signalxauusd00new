import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.jobs import run_analysis
from services.telegram_service import bot, dp

from pytz import utc

scheduler = AsyncIOScheduler(timezone=utc)


# tiap jam menit 00
scheduler.add_job(run_analysis, "cron", minute=0)


async def main():

    print("BOT RUNNING...")

    scheduler.start()

    # INI YANG ENABLE /harga
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
