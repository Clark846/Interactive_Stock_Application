import matplotlib
import pandas as pd
import numpy as np
import scipy as stats
from pandas_datareader import data as pdr
import datetime as dt

import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf

'Scales for window size '
res_width = 2000
res_height = 2000
'========================================================================================='
yf.pdr_override()
#stockTicker = input(str("Search Stock: "))
#stockTicker.upper()

'Input functions'
stockTicker = input(str("Search Stock: "))
ChartType = input(str("What type of Chart would you prefer(Candle|Line|Renko|Hollow): "))
ChartType = ChartType.lower()
#interval = input(str("Input timeframe:  ")) + 'm'
stockTicker = stockTicker.upper()
#========================================================================
start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()

"Pulls Stock Data from Yahoo"
#data = yf.Ticker(stockTicker).history(start, end)
data = yf.download(stockTicker,start,end)
data = data.loc["2021-01-01":]

'Customize Colors for CandleSticks on Chart'
colors = mpf.make_marketcolors(up="#00ff00",
                               down="#ff0000",
                               wick="inherit",
                               edge="inherit",
                               volume="in")
'Chart Types''---------------------------------------------------------------------'
#'binance', 'binancedark', 'blueskies', 'brasil', 'charles', 'checkers', 'classic',
#'default', 'ibd', 'kenan', 'mike', 'nightclouds', 'sas', 'starsandstripes', 'tradingview', 'yahoo']

mpf_style = mpf.make_mpf_style(base_mpf_style = "binance", marketcolors = colors ,facecolor= '#202020', figcolor = "#787878")

#=====================================================================================
#=====================================================================================
'Support and Resistance Functions'
Support = data[data.Low == data.Low.rolling(5, center=True).min()].Low
Resistance = data[data.High == data.High.rolling(5, center=True).max()].High

Levels = pd.concat([Support, Resistance])
Levels = Levels[abs(Levels.diff()) > 70 ]

#=====================================================================================
"Plots Data"
mpf.plot(data, type=ChartType, hlines=Levels.to_list(), style=mpf_style, mav= 20, axtitle=stockTicker,
               figsize=(0.7*res_width/100, 0.45*res_height/100) , scale_padding={'left': 1, 'top': 2, 'right': 3.5, 'bottom': 1 }, tight_layout=True,
               volume=True)
