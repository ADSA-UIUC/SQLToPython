
import urllib2
from bs4 import BeautifulSoup              # import required modules for web scraping

names=["GPS", "NFLX", "GRPN", "INTC", "AAPL", "MOLG", "WAIR", "OTIV", "AMDA", "ARUN", "ICLDW", "AAPL", "GOOG", "BABA"]

def calc(names):        # method declaration
    for i in names:         # loop start to use the yahoo finace link on each stock name
        url = 'http://finance.yahoo.com/q?s='+i     # the url to visit and scrape for news articles
        data = urllib2.urlopen(url)                 # getting the data from the page
        soup = BeautifulSoup(data)                  # letting beautiful soup 4 work its magic on the data
        
        divs = soup.find('div',attrs={'id':'yfi_headlines'})        # looking for the particular tag
        div = divs.find('div',attrs={'class':'bd'})             # looking for a tag under a tag
        ul = div.find('ul')
        lis = ul.findAll('li')
        print i             # print the stock you are now dealing with
        m=0.0               # score saver for results on using sentiment analysis
        for li in lis:          # looping through tags that match the required web scraping criteria
            headlines = li.find('a').get('href')        # getting the url in the tags, linking to actual articles
            print headlines
            ur='http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=9b61009a54069badce0cc7ed6bc3f229b07d150a&url='+headlines
            dat=urllib2.urlopen(ur)             # beautiful soup again but on the sentiment analysis results
            sou=BeautifulSoup(dat)          # beautiful soup again but on the sentiment analysis results
            if sou.find('score')!=None:
                m+=float(sou.find('score').string)
    return m
        
print calc(names)       # print the output
