import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
FINNHUB_TOKEN = os.getenv("FINNHUB_TOKEN")
TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY")

CHAT_ID = os.getenv("CHAT_ID")
CHAT_ID = int(CHAT_ID) if CHAT_ID else None

PAIR = "OANDA:XAU_USD"
