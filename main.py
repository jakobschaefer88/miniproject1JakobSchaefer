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

myTickers = ["WMT", "AAPL", "GDDY", "F", "WEN"]
myData = {}

myTickers.sort()
for ticker in myTickers:
    result = yf.Ticker(ticker)
    myData[ticker] = {'ticker': ticker,
                      'dailyHigh': result.info['dayHigh']
                     }
    #pprint.pprint(myData)
    #print(f"Ticker: {ticker} \tDaily High: {result.info['dayHigh']}")

pprint.pprint(myData)
# get all stock info
#pprint.pprint(wmt.info)

# get historical market data
#hist = msft.history(period="1mo")
#pprint.pprint(hist)