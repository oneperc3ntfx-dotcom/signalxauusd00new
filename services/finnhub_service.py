import requests
from config import FINNHUB_API_KEY

BASE_URL = "https://finnhub.io/api/v1"


# =========================
# REALTIME PRICE
# =========================
def get_realtime_price(symbol="OANDA:XAU_USD"):

    try:
        url = (
            f"{BASE_URL}/quote"
            f"?symbol={symbol}"
            f"&token={FINNHUB_API_KEY}"
        )

        res = requests.get(url, timeout=10)
        data = res.json()

        price = data.get("c", None)

        if price is None or price == 0:
            print("Finnhub invalid price:", data)
            return None

        return float(price)

    except Exception as e:
        print("Finnhub exception:", e)
        return None
