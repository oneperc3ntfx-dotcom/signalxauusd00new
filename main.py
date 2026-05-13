from apscheduler.schedulers.blocking import BlockingScheduler
from scheduler.jobs import run_analysis
from pytz import utc

scheduler = BlockingScheduler(timezone=utc)

# jalan setiap jam menit 00
scheduler.add_job(
    run_analysis,
    'cron',
    minute=0
)

print("XAUUSD BOT RUNNING...")

# test pertama
run_analysis()

scheduler.start()
