# -*- coding: utf-8 -*-

import os
import sys
import asciichart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------

this_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(os.path.dirname(this_folder))
sys.path.append(root_folder + '/python')
sys.path.append(this_folder)

# -----------------------------------------------------------------------------

import ccxt  # noqa: E402

# -----------------------------------------------------------------------------

kraken = ccxt.kraken()
gdax = ccxt.gdax()

symbol = 'BTC/USD'

# each ohlcv candle is a list of [ timestamp, open, high, low, close, volume ]
index = 4  # use close price from each ohlcv candle


def print_chart(exchange, symbol, timeframe):

    print("\n" + exchange.name + ' ' + symbol + ' ' + timeframe + ' chart:')

    # get a list of ohlcv candles
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

    # get the ohlCv (closing price, index == 4)
    series = [x[index] for x in ohlcv]
    time = [t[0] for t in ohlcv]

    tframe = pd.DataFrame(time)
    frame = pd.DataFrame(series)
    #print("enter")
    print("\n" + frame[-2:].to_string())
    print("\n" + tframe[-2:].to_string())

    #ts = pd.Series(frame[-150:], tframe[-150:])
    #ts = ts.cumsum()
    #ts.plot()

    #ts = pd.Series(np.random.randn(1000),
    #index=pd.date_range('1/1/2000', periods=1000))

    #ts = ts.cumsum()
    fig = plt.figure()
    #plt.plot(1,1)
    #plt.show()

    # print the chart
    print("\n" + asciichart.plot(series[-150:], {'height': 20}))  # print the chart

    last = ohlcv[len(ohlcv) - 1][index]  # last closing price
    return last

#def panPrint(exchange, symbol, timeframe):

    #price = exchange.fetch_ohlcv(symbol, timeframe)

last = print_chart(kraken, 'BTC/USD', '1h')
print("\n" + kraken.name + " ₿ = $" + str(last) + "\n")  # print last closing price

last = print_chart(gdax, 'BTC/USD', '1h')
print("\n" + gdax.name + " ₿ = $" + str(last) + "\n")  # print last closing price
