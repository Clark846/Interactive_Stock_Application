#Original Code
import matplotlib
from pandas_datareader import data as pdr
from mpl_interactions import ioff, panhandler, zoom_factory
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf

'========================================================================================='
yf.pdr_override()
stockTicker = input(str("Search Stock: "))


start = dt.datetime(1999, 1, 1)
end = dt.datetime.now()

data = pdr.get_data_yahoo(stockTicker, start, end)
#data = web.DataReader(stockTicker,'yahoo', start, end)

colors = mpf.make_marketcolors(up = "#00ff00",
                               down = "#ff0000",
                               wick = "inherit",
                               edge = "inherit",
                               volume = "in")

mpf_style = mpf.make_mpf_style(base_mpf_style = "nightclouds", marketcolors = colors)
mpf.plot(data, type="candle", style=mpf_style, axtitle=stockTicker, volume=True)

