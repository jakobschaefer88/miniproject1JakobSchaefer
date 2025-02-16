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

#imports
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

#checks to see if charts folder exists, if not creates it
os.makedirs("charts", exist_ok=True)

#sets today as today's date
today = datetime.today()

#sets the last 10 business days from todays date,
ten_days_ago = today - timedelta(days=15)

#my favorite Tickets
myTickers = ["WMT", "AAPL", "GDDY", "F", "WEN"]

#for loop for myTickers to loop through each one
for ticker in myTickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10Days = []
    #for loop to go through and show the date from the last 10 days
    for date in hist['Close'][:11]:
        last10Days.append(date)
    #if loop for creating the graph from the last 10 days at 1 percent above and below the closing price
    if len(last10Days) ==10:
        myArray = np.array(last10Days)
        maxPrice = myArray.max() + (myArray.max() * .01)
        minPrice = myArray.min() - (myArray.min() * .01)
        plt.plot(myArray)
        plt.xlabel('Days ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, minPrice, maxPrice))
        plt.title(f"{ticker} last 10 closing prices")
        plt.savefig(f"charts/{ticker}.png")
    #if the data doesn't have 10 days, exports doesn't have 10 days
    else:
        print(f"Do not have 10 days of data. Only has {len(last10Days)} days.")
