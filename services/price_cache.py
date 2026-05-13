import time
from services.finnhub_service import get_realtime_price

last_price = None
last_update = 0

CACHE_SECONDS = 5


def update_price():

    global last_price, last_update

    price = get_realtime_price()

    if price is not None:
        last_price = price
        last_update = time.time()


def get_cached_price():

    global last_price, last_update

    if last_price is None or (time.time() - last_update) > CACHE_SECONDS:
        update_price()

    return last_price
