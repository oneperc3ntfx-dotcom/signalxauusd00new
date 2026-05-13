from services.mt5_service import get_candles
from strategy.scoring import calculate_score
from utils.helpers import generate_signal
from services.telegram_service import send_telegram
from config import SYMBOL


def run_analysis():
    try:
        df = get_candles(SYMBOL)

        score = calculate_score(df)
        signal = generate_signal(score)

        current_price = round(df.iloc[-1]['close'], 2)

        if signal == "BUY":
            sl = round(current_price - 5, 2)
            tp = round(current_price + 10, 2)

            message = f'''
XAUUSD BUY

Entry: {current_price}
SL: {sl}
TP: {tp}

Score: {score}
'''

        elif signal == "SELL":
            sl = round(current_price + 5, 2)
            tp = round(current_price - 10, 2)

            message = f'''
XAUUSD SELL

Entry: {current_price}
SL: {sl}
TP: {tp}

Score: {score}
'''

        else:
            message = f'''
XAUUSD HOLD

No valid setup.
Score: {score}
'''

        print(message)

        send_telegram(message)

    except Exception as e:
        print(f"ERROR: {e}")
