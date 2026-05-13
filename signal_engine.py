def analyze_m5(candles):

    if len(candles) < 10:
        return None, None

    closes = [float(c["close"]) for c in candles]

    trend = "UP" if closes[-1] > closes[0] else "DOWN"

    high = max(float(c["high"]) for c in candles)
    low = min(float(c["low"]) for c in candles)
    volatility = high - low

    if trend == "UP" and volatility > 5:
        return "BUY", {
            "trend": trend,
            "volatility": volatility
        }

    if trend == "DOWN" and volatility > 5:
        return "SELL", {
            "trend": trend,
            "volatility": volatility
        }

    return None, {
        "trend": trend,
        "volatility": volatility
    }
