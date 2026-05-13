from strategy.momentum import calculate_momentum
from strategy.volatility import calculate_atr
from strategy.breakout import breakout_signal


def calculate_score(df):

    score = 0

    momentum = calculate_momentum(df)
    atr = calculate_atr(df)
    breakout = breakout_signal(df)

    # momentum
    if momentum["bull_power"] > momentum["bear_power"]:
        score += 2
    else:
        score -= 2

    # candle dominance
    if momentum["bullish_count"] >= 8:
        score += 2

    if momentum["bearish_count"] >= 8:
        score -= 2

    # volatility filter
    if atr > 2:
        score += 2 if score > 0 else -2

    # breakout
    if breakout == "BUY":
        score += 3

    if breakout == "SELL":
        score -= 3

    return score
