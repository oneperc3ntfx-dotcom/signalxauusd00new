from apscheduler.schedulers.blocking import BlockingScheduler
from scheduler.jobs import run_analysis
from services.mt5_service import initialize_mt5
from pytz import utc

initialize_mt5()

scheduler = BlockingScheduler(timezone=utc)

# Jalan setiap jam menit 00
scheduler.add_job(
    run_analysis,
    'cron',
    minute=0
)

print("XAUUSD BOT RUNNING...")

run_analysis()

scheduler.start()
