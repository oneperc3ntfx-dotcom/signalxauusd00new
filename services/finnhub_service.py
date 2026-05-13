import requests
import pandas as pd
import time
from config import FINNHUB_API_KEY

BASE_URL = "https://finnhub.io/api/v1"


# =========================
# REALTIME PRICE
# =========================
def get_realtime_price(symbol="OANDA:XAU_USD"):

    url = (
        f"{BASE_URL}/quote"
        f"?symbol={symbol}"
        f"&token={FINNHUB_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    # safety check
    if "c" not in data:
        print("Realtime error:", data)
        return None

    return data["c"]


# =========================
# 12 CANDLE M5 HISTORY
# =========================
def get_candles(symbol="OANDA:XAU_USD", resolution="5", count=12):

    try:
        now = int(time.time())

        # ambil lebih lebar biar tidak kosong
        from_time = now - (60 * 60 * 2)  # 2 jam data

        url = (
            f"{BASE_URL}/stock/candle"
            f"?symbol={symbol}"
            f"&resolution={resolution}"
            f"&from={from_time}"
            f"&to={now}"
            f"&token={FINNHUB_API_KEY}"
        )

        response = requests.get(url)
        data = response.json()

        # =========================
        # VALIDASI RESPONSE
        # =========================
        if data.get("s") != "ok":
            print("Finnhub error:", data)
            return None

        if "t" not in data or len(data["t"]) == 0:
            print("Empty candle data:", data)
            return None

        df = pd.DataFrame({
            "time": data["t"],
            "open": data["o"],
            "high": data["h"],
            "low": data["l"],
            "close": data["c"],
            "volume": data["v"]
        })

        df["time"] = pd.to_datetime(df["time"], unit="s")

        # ambil 12 candle terakhir
        df = df.tail(count)

        return df

    except Exception as e:
        print("Candle fetch error:", e)
        return None
