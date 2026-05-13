def breakout_signal(df):

    last = df.iloc[-1]

    highest = df['high'][:-1].max()
    lowest = df['low'][:-1].min()

    # breakout atas
    if last['close'] > highest:
        return "BUY"

    # breakout bawah
    if last['close'] < lowest:
        return "SELL"

    return "NONE"
