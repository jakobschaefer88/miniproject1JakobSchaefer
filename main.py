'''
INF601 - Programming in Python
Assignment 1
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

### INF601 - Advanced Programming in Python
### Jakob Schaefer
### Mini Project 1

import yfinance as yf
import pprint
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

# Get today's date
today = datetime.today()

# Subtract 10 days
ten_days_ago = today - timedelta(days=15)

myTickers = ["WMT", "AAPL", "GDDY", "F", "WEN"]
myData = {}

myTickers.sort()
for ticker in myTickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)

    last10Days = []
    for date in hist['Close'][:11]:
        last10Days.append(date)
    if len(last10Days) ==10:
        myarray = np.array(last10Days)
        maxPrice = myarray.max() + (myarray.max() * .01)
        minPrice = myarray.min() - (myarray.min() * .01)
        plt.plot(myarray)
        plt.xlabel('Days ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, minPrice, maxPrice))
        plt.title(f"{ticker} last 10 closing prices")
        plt.show()
    else:
        print(f"Do not have 10 days of data. Only has {len(last10Days)} days.")


# get all stock info
#pprint.pprint(wmt.info)

# get historical market data
#hist = msft.history(period="1mo")
#pprint.pprint(hist)