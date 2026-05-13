import json
import asyncio
import websockets
from config import FINNHUB_TOKEN, PAIR

state = {"price": None}

def get_last_price():
    return state["price"]


async def stream_price(lock):

    url = f"wss://ws.finnhub.io?token={FINNHUB_TOKEN}"

    while True:
        try:
            async with websockets.connect(url) as ws:

                await ws.send(json.dumps({
                    "type": "subscribe",
                    "symbol": PAIR
                }))

                print("Finnhub WS connected")

                async for msg in ws:

                    data = json.loads(msg)

                    if data.get("type") == "trade":

                        for t in data["data"]:

                            async with lock:
                                state["price"] = float(t["p"])

        except Exception as e:
            print("WS reconnect:", e)
            await asyncio.sleep(3)
