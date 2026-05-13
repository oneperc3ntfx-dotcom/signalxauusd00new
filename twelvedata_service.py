import requests
from config import TWELVEDATA_API_KEY

BASE_URL = "https://api.twelvedata.com"


def get_candles(symbol="XAU/USD", interval="5min", limit=12):

    if not TWELVEDATA_API_KEY:
        print("TwelveData error: API key missing")
        return []

    try:
        url = (
            f"{BASE_URL}/time_series"
            f"?symbol={symbol}"
            f"&interval={interval}"
            f"&outputsize=50"
            f"&apikey={TWELVEDATA_API_KEY}"
        )

        res = requests.get(url, timeout=10)
        data = res.json()

        if "values" not in data:
            print("TwelveData error:", data)
            return []

        values = data["values"][:limit]
        values = list(reversed(values))

        # convert to float safely
        candles = []

        for v in values:
            candles.append({
                "open": float(v["open"]),
                "high": float(v["high"]),
                "low": float(v["low"]),
                "close": float(v["close"]),
            })

        return candles

    except Exception as e:
        print("TwelveData error:", e)
        return []
