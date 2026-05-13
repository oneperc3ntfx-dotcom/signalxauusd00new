import requests
from config import TWELVEDATA_API_KEY

BASE_URL = "https://api.twelvedata.com"


# =========================
# GET 12 CANDLES M5
# =========================
def get_m5_candles(symbol="XAU/USD", limit=12):

    url = (
        f"{BASE_URL}/time_series"
        f"?symbol={symbol}"
        f"&interval=5min"
        f"&outputsize={limit}"
        f"&apikey={TWELVEDATA_API_KEY}"
    )

    res = requests.get(url, timeout=10)
    data = res.json()

    if "values" not in data:
        return []

    return list(reversed(data["values"]))
