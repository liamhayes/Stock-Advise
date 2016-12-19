# Stock-Advise
This program scrapes data of of Nasdaq.com and uses it to make some calculations (sentiment, and extimated 1 year price) regarding the stocks valuation. The outcomes of those calculations are rated based on a score of 1-10
Those ratings are then averaged. It then prints out a response based on whether or not you should purchase the stock.
I hope to implement the smtplib so it can email the outcomes of the tests.

Dependencies:
yahoo-finance module
re
urllib
