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

        # ambil 12 candle history
        df = get_candles(SYMBOL)

        # hitung strategy score
        score = calculate_score(df)

        # generate BUY SELL HOLD
        signal = generate_signal(score)

        # realtime entry price
        realtime_price = round(
            get_realtime_price(SYMBOL),
            2
        )

        # BUY
        if signal == "BUY":

            sl = round(realtime_price - 5, 2)
            tp = round(realtime_price + 10, 2)

            message = f"""
XAUUSD BUY

Realtime Entry:
{realtime_price}

SL:
{sl}

TP:
{tp}

Score:
{score}

Engine:
Momentum + Volatility
"""

        # SELL
        elif signal == "SELL":

            sl = round(realtime_price + 5, 2)
            tp = round(realtime_price - 10, 2)

            message = f"""
XAUUSD SELL

Realtime Entry:
{realtime_price}

SL:
{sl}

TP:
{tp}

Score:
{score}

Engine:
Momentum + Volatility
"""

        # HOLD
        else:

            message = f"""
XAUUSD HOLD

No valid setup

Realtime Price:
{realtime_price}

Score:
{score}
"""

        print(message)

        # kirim telegram
        send_telegram(message)

    except Exception as e:

        print(f"ERROR: {e}")
