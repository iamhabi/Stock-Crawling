import json
import requests
from bs4 import BeautifulSoup

import sise_day as sd
import news
import main_news as mn
import stock_market as sm
import exchange_rate as er
import gold

kcodes = ["005930", "000660", "051910", "006400", "035720", "035420", "005380", "066570", "034220"]
acodes = ["MSFT", "AAPL", "TSLA", "AMZN"]

naverURL = "https://finance.naver.com/item/sise.nhn?code="
yahooURL = "https://finance.yahoo.com/quote/"

stocks = []

def get_stock_naver(code):
    result = requests.get(naverURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.select_one('div.wrap_company > h2').text
    rate = soup.select_one('div.rate_info > div.today > p > em > span.blind').text


    stock = {}
    stock['title'] = title
    stock['code'] = code
    stock['rate'] = rate

    # get stock quotations
    stock_day = sd.get_sise_day_naver(code)
    stock['sd'] = stock_day
    
    # get stock news
    news_day = news.get_news_naver(code)
    stock['news'] = news_day

    stocks.append(stock)

def get_stock_yahoo(code):
    result = requests.get(yahooURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.select_one('h1').text
    rate = soup.select_one('span[data-reactid="32"]').text

    stock = {}
    stock['title'] = title
    stock['code'] = code
    stock['rate'] = rate

    # get stock quotations
    stock_day = sd.get_sise_day_yahoo(code)
    stock['sd'] = stock_day

    #get stock news
    news_day = news.get_news_yahoo(code)
    stock['news'] = news_day

    stocks.append(stock)

data = {}

with open('stock.json', 'w') as f:
    json.dump(data, f, indent = 4)

# main news
mn.get_mn()

# Stock Market ex) KOSPI, NASDAQ
sm.get_stock_market()

# Exchange Rate ex) USDKRW, EURKRW
er.get_er()

# Gold
gold.get_gold()

# Stock
for code in kcodes:
    get_stock_naver(code)

for code in acodes:
    get_stock_yahoo(code)

# save stocks as json
with open('stock.json', 'r') as f:
    json_data = json.load(f)

json_data['stocks'] = stocks

with open('stock.json', 'w', encoding = 'utf-8') as f:
    json.dump(json_data, f, indent = 4, ensure_ascii = False)