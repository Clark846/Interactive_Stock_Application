# import matplotlib.pyplot as plt
# import pandas_datareader as web
# import mplfinance as mpf
# import datetime as dt
# #import yfinance as yf
#
# start = dt.datetime(2019, 1, 1)
# end = dt.datetime.now()
#
# data = web.DataReader('SPY', 'stooq', start, end)
#
# #plt.plot(data['Close'])
# #plt.show()
# #mpf.plot(data, type = "candle")
# #print(mpf.available_styles())
#
# colors = mpf.make_marketcolors(up = "#00ff00",
#                                down = "#ff0000",
#                                wick = "inherit",
#                                edge = "inherit",
#                                volume = "in")
#
# mpf_style = mpf.make_mpf_style(base_mpf_style = "nightclouds", marketcolors = colors)
# mpf.plot(data,type = "candle" , style = mpf_style, volume = True )
#
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

from polygon import RESTClient
client = RESTClient(api_key="<LFGoeNO5GiDrupSdSSb5vdZuwzberOWc")
ticker = "SPY"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

#Define Time Frame
start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

#Load Data
#Use stooq if yahoo doesn't work
#data = web.DataReader('SPY', 'LFGoeNO5GiDrupSdSSb5vdZuwzberOWc', start, end)

print(aggs)