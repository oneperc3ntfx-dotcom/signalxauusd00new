from services.twelvedata_service import get_candles
from services.finnhub_service import get_realtime_price

from strategy.scoring import calculate_score
from utils.helpers import generate_signal
from services.telegram_service import send_telegram
from config import SYMBOL


def run_analysis():

    try:

        # =========================
        # CANDLE (TWELVE DATA)
        # =========================
        df = get_candles(SYMBOL)

        if df is None or df.empty:
            print("No candle data")
            return

        # =========================
        # ANALISA
        # =========================
        score = calculate_score(df)
        signal = generate_signal(score)

        # =========================
        # REALTIME PRICE (FINNHUB)
        # =========================
        price = get_realtime_price(SYMBOL)

        if price is None:
            print("No price from Finnhub")
            return

        entry = round(price, 2)

        # =========================
        # OUTPUT SIGNAL
        # =========================
        if signal == "BUY":

            msg = f"""
XAUUSD BUY

Entry: {entry}
Score: {score}
"""

        elif signal == "SELL":

            msg = f"""
XAUUSD SELL

Entry: {entry}
Score: {score}
"""

        else:

            msg = f"""
XAUUSD HOLD

Price: {entry}
Score: {score}
"""

        print(msg)
        send_telegram(msg)

    except Exception as e:
        print("JOB ERROR:", e)
