import asyncio
from datetime import datetime, timedelta
from config import CHAT_ID
from data_feed import get_last_price
from twelvedata_service import get_m5_candles
from signal_engine import analyze_m5


# ================= MODE JAM 00 =================
async def hourly_scheduler(app):

    last_run = None

    while True:

        now = datetime.now()

        next_run = now.replace(minute=0, second=0, microsecond=0)

        if now.minute != 0:
            next_run += timedelta(hours=1)

        await asyncio.sleep((next_run - now).total_seconds())

        key = now.strftime("%Y-%m-%d %H")
        if key == last_run:
            continue

        candles = get_m5_candles()

        signal, meta = analyze_m5(candles)

        price = get_last_price()

        if signal:

            msg = f"""
📊 XAUUSD SIGNAL (HOURLY)

📈 {signal}
📊 Trend: {meta['trend']}
📉 Volatility: {meta['volatility']:.2f}
💰 Price: {price}
"""

            await app.bot.send_message(chat_id=CHAT_ID, text=msg)

        last_run = key


# ================= MODE PRO MAX (5 MIN) =================
async def pro_max_scheduler(app):

    while True:

        candles = get_m5_candles()

        signal, meta = analyze_m5(candles)

        price = get_last_price()

        if signal:

            msg = f"""
🔥 PRO MAX SIGNAL

📈 {signal}
📊 Trend: {meta['trend']}
📉 Volatility: {meta['volatility']:.2f}
💰 Price: {price}
"""

            await app.bot.send_message(chat_id=CHAT_ID, text=msg)

        await asyncio.sleep(300)
