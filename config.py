import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
FINNHUB_TOKEN = os.getenv("FINNHUB_TOKEN")

TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY")

CHAT_ID = os.getenv("CHAT_ID")
CHAT_ID = int(CHAT_ID) if CHAT_ID else None

THREAD_ID = os.getenv("THREAD_ID")
THREAD_ID = int(THREAD_ID) if THREAD_ID else 0

PAIR = "OANDA:XAU_USD"
