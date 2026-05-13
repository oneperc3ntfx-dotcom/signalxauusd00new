import json
import asyncio
import websockets
from config import FINNHUB_TOKEN, PAIR

state = {"price": None}

def get_last_price():
    return state["price"]


async def stream_price(lock):

    url = f"wss://ws.finnhub.io?token={FINNHUB_TOKEN}"

    retry_delay = 2

    while True:
        try:
            async with websockets.connect(
                url,
                ping_interval=20,
                ping_timeout=20
            ) as ws:

                await ws.send(json.dumps({
                    "type": "subscribe",
                    "symbol": PAIR
                }))

                print("Finnhub WS connected")

                retry_delay = 2  # reset kalau sukses

                async for msg in ws:

                    data = json.loads(msg)

                    if data.get("type") == "trade":

                        for t in data["data"]:

                            async with lock:
                                state["price"] = float(t["p"])

        except Exception as e:

            print(f"WS reconnect: {e}")

            await asyncio.sleep(retry_delay)

            # exponential backoff
            retry_delay = min(retry_delay * 2, 30)
