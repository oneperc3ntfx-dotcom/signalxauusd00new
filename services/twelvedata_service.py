import requests
import pandas as pd
from config import TWELVEDATA_API_KEY

BASE_URL = "https://api.twelvedata.com"


# =========================
# CANDLE HISTORY (12 M5)
# =========================
def get_candles(symbol="XAU/USD", interval="5min", outputsize=12):

    url = (
        f"{BASE_URL}/time_series"
        f"?symbol={symbol}"
        f"&interval={interval}"
        f"&outputsize=50"
        f"&apikey={TWELVEDATA_API_KEY}"
    )

    res = requests.get(url)
    data = res.json()

    if "values" not in data:
        print("TwelveData error:", data)
        return None

    df = pd.DataFrame(data["values"])

    # normalize
    df = df.rename(columns={
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close",
        "volume": "volume",
        "datetime": "time"
    })

    df = df.astype({
        "open": float,
        "high": float,
        "low": float,
        "close": float
    })

    df = df.head(outputsize)
    df = df.iloc[::-1]  # urutkan ke lama -> baru

    return df
