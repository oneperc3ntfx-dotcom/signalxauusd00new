import requests
from config import TWELVEDATA_API_KEY

BASE_URL = "https://api.twelvedata.com"


def get_m5_candles(symbol="XAU/USD", interval="5min", limit=12):

    if not TWELVEDATA_API_KEY:
        print("TwelveData error: missing API key")
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

        values = list(reversed(data["values"][:limit]))

        return [
            {
                "open": float(v["open"]),
                "high": float(v["high"]),
                "low": float(v["low"]),
                "close": float(v["close"]),
            }
            for v in values
        ]

    except Exception as e:
        print("TwelveData error:", e)
        return []


# ================= COMPATIBILITY LAYER =================
get_candles = get_m5_candles
