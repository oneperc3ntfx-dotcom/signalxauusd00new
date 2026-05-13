import requests
import pandas as pd
from config import TWELVEDATA_API_KEY

BASE_URL = "https://api.twelvedata.com"


# =========================
# CANDLE HISTORY ONLY
# =========================
def get_candles(symbol="XAU/USD", interval="5min", limit=12):

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
            return None

        df = pd.DataFrame(data["values"])

        df = df[["open", "high", "low", "close"]].astype(float)

        df = df.head(limit)
        df = df.iloc[::-1]

        return df

    except Exception as e:
        print("TwelveData exception:", e)
        return None
