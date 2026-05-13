def generate_signal(score):

    if score >= 7:
        return "BUY"

    if score <= -7:
        return "SELL"

    return "HOLD"
