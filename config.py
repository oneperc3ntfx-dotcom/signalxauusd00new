import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SYMBOL = os.getenv("SYMBOL", "XAUUSD")

TIMEFRAME = "M5"
CANDLE_COUNT = 12

BUY_THRESHOLD = 7
SELL_THRESHOLD = -7
