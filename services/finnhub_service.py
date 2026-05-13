import requests
from config import FINNHUB_TOKEN, PAIR

BASE_URL = "https://finnhub.io/api/v1"


def get_realtime_price():

    try:
        url = f"{BASE_URL}/quote?symbol={PAIR}&token={FINNHUB_TOKEN}"

        res = requests.get(url, timeout=10)
        data = res.json()

        price = data.get("c")

        if price is None or price == 0:
            print("Finnhub invalid:", data)
            return None

        return float(price)

    except Exception as e:
        print("Finnhub error:", e)
        return None
