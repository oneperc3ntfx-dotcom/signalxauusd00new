import requests
import pandas as pd
import time

from config import FINNHUB_API_KEY

BASE_URL = "https://finnhub.io/api/v1"


# realtime price
def get_realtime_price(symbol="OANDA:XAU_USD"):

    url = (
        f"{BASE_URL}/quote"
        f"?symbol={symbol}"
        f"&token={FINNHUB_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    return data['c']


# ambil 12 candle M5
def get_candles(
    symbol="OANDA:XAU_USD",
    resolution="5",
    count=12
):

    now = int(time.time())

    # 12 candle x 5 menit
    from_time = now - (count * 5 * 60)

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

    df = pd.DataFrame({
        'time': data['t'],
        'open': data['o'],
        'high': data['h'],
        'low': data['l'],
        'close': data['c'],
        'volume': data['v']
    })

    df['time'] = pd.to_datetime(df['time'], unit='s')

    return df
