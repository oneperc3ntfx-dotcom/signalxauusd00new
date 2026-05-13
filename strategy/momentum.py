def calculate_momentum(df):
    bull_power = 0
    bear_power = 0

    bullish_count = 0
    bearish_count = 0

    for _, candle in df.iterrows():
        body = candle['close'] - candle['open']

        if body > 0:
            bull_power += abs(body)
            bullish_count += 1
        else:
            bear_power += abs(body)
            bearish_count += 1

    return {
        "bull_power": bull_power,
        "bear_power": bear_power,
        "bullish_count": bullish_count,
        "bearish_count": bearish_count
    }
