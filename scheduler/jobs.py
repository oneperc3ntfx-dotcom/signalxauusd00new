from services.finnhub_service import (
    get_candles,
    get_realtime_price
)

from strategy.scoring import calculate_score
from utils.helpers import generate_signal
from services.telegram_service import send_telegram
from config import SYMBOL


def run_analysis():

    try:

        # =========================
        # AMBIL DATA CANDLE
        # =========================
        df = get_candles(SYMBOL)

        # ❌ HANDLE KOSONG
        if df is None or df.empty:
            print("No candle data - SKIP")
            return

        # =========================
        # HITUNG SIGNAL
        # =========================
        score = calculate_score(df)
        signal = generate_signal(score)

        # =========================
        # AMBIL HARGA REALTIME
        # =========================
        price = get_realtime_price(SYMBOL)

        # ❌ HANDLE REALTIME ERROR
        if price is None:
            print("No realtime price - SKIP")
            return

        realtime_price = round(price, 2)

        # =========================
        # BUILD MESSAGE
        # =========================
        if signal == "BUY":

            sl = round(realtime_price - 5, 2)
            tp = round(realtime_price + 10, 2)

            message = f"""
XAUUSD BUY

Entry: {realtime_price}
SL: {sl}
TP: {tp}

Score: {score}
"""

        elif signal == "SELL":

            sl = round(realtime_price + 5, 2)
            tp = round(realtime_price - 10, 2)

            message = f"""
XAUUSD SELL

Entry: {realtime_price}
SL: {sl}
TP: {tp}

Score: {score}
"""

        else:

            message = f"""
XAUUSD HOLD

No valid setup

Price: {realtime_price}
Score: {score}
"""

        print(message)

        send_telegram(message)

    except Exception as e:
        print("JOB ERROR:", e)
