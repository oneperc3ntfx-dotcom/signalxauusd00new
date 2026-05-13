import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime


def initialize_mt5():
    if not mt5.initialize():
        raise Exception("MT5 initialization failed")


def get_candles(symbol, count=12):
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, count)

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')

    return df
