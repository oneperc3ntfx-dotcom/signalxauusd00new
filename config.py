import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Finnhub
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

# Symbol Gold
SYMBOL = "OANDA:XAU_USD"

# Strategy Setting
TIMEFRAME = "5"
CANDLE_COUNT = 12

# Threshold
BUY_THRESHOLD = 7
SELL_THRESHOLD = -7
