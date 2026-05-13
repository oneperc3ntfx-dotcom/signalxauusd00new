def calculate_atr(df):

    highs = df['high']
    lows = df['low']

    atr = (highs - lows).mean()

    return atr
