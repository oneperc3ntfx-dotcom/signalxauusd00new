import requests
from config import FINNHUB_API_KEY

BASE_URL = "https://finnhub.io/api/v1"


def get_realtime_price(symbol="OANDA:XAU_USD"):

    url = (
        f"{BASE_URL}/quote"
        f"?symbol={symbol}"
        f"&token={FINNHUB_API_KEY}"
    )

    res = requests.get(url)
    data = res.json()

    if "c" not in data:
        print("Finnhub realtime error:", data)
        return None

    return data["c"]
