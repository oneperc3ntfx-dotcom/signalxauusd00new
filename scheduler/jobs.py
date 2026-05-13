from services.twelvedata_service import get_candles
from services.finnhub_service import get_realtime_price

from strategy.scoring import calculate_score
from utils.helpers import generate_signal
from services.telegram_service import send_telegram
from config import SYMBOL


def run_analysis():

    try:

        # =========================
        # CANDLE ANALYSIS (TWELVE DATA)
        # =========================
        df = get_candles(SYMBOL)

        if df is None or df.empty:
            print("No TwelveData candles")
            return

        score = calculate_score(df)
        signal = generate_signal(score)

        # =========================
        # REALTIME PRICE (FINNHUB)
        # =========================
        price = get_realtime_price(SYMBOL)

        if price is None:
            print("No Finnhub price")
            return

        entry = round(price, 2)

        # =========================
        # SIGNAL OUTPUT
        # =========================
        if signal == "BUY":

            sl = round(entry - 5, 2)
            tp = round(entry + 10, 2)

            msg = f"""
XAUUSD BUY

Entry: {entry}
SL: {sl}
TP: {tp}

Score: {score}
"""

        elif signal == "SELL":

            sl = round(entry + 5, 2)
            tp = round(entry - 10, 2)

            msg = f"""
XAUUSD SELL

Entry: {entry}
SL: {sl}
TP: {tp}

Score: {score}
"""

        else:

            msg = f"""
XAUUSD HOLD

No setup

Price: {entry}
Score: {score}
"""

        print(msg)
        send_telegram(msg)

    except Exception as e:
        print("ERROR:", e)
