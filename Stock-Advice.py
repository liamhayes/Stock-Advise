import urllib
import re
import smtplib
import yahoo_finance as yahoo

stock_score = 0

#input of stock symbol here
symbol = raw_input('Stock Symbol: ')

#yahoo finance stock price stuff here
share = yahoo.Share(symbol)
rawstock = share.get_price()
stock_price = float(rawstock)           #converts stock_price to integer so I can make mathematical equation with it 


def get_target_Price():
    global stock_score
    stock_score = 0
    url = 'http://www.nasdaq.com/symbol/'+symbol+'/real-time'
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="quotes_content_left__1YearTargetEstimate">(.+?)</span>'
    pattern = re.compile(regex)
    target = re.findall(pattern,htmltext)
    str1 = ''.join(target)              #converts target to string so I will be able to delete $ sign
    str2 = str1.replace('$','')
    target_price = int(str2)
    
    if target_price > stock_price * 1.25 :
        
        stock_score += 10
    elif target_price > stock_price * 1.1:
        
        stock_score += 5
    else:
        
        stock_score += 0
        
get_target_Price()        
    
        
def get_sentiment():
    global sentiment_score
    sentiment_score = 0
    url = 'http://www.nasdaq.com/symbol/'+symbol+'/real-time'
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="quotes_content_left_OverallStockRating1_lblPercentage" class="comm_bullrating">(.+?)</span>'
    pattern = re.compile(regex)
    sentiment = re.findall(pattern,htmltext)
    str1 = ''.join(sentiment)
    str2 = str1.replace('% bullish','')
    sentiment_int = str2
    
    if sentiment_int > 90 :
        
        sentiment_score += 10
        
    elif  sentiment_int > 80:
        
        sentiment_score += 5
        
    else:
        sentiment_score += 0


   
get_sentiment()
        
        
        
if ((sentiment_score + stock_score) / 2) > 7.5:
    print ('I advise you to buy %s , it is likely to become profitable' % symbol)         
        
        
if ((sentiment_score + stock_score) / 2) >= 5:
    print ('There is potential that %s might be profitable' % symbol)
    
elif ((sentiment_score + stock_score) / 2) < 4.99:
        print ('I would advise aganst buying %s' % symbol)