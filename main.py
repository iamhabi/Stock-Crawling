import json
import requests
from bs4 import BeautifulSoup

import sise_day as sd
import news
import main_news as mn

codes = ["005930", "000660", "051910", "006400", "035720", "035420", "005380", "066570", "034220"]
siseURL = "https://finance.naver.com/item/sise.nhn?code="

stocks = []

def get_stock(code):
    result = requests.get(siseURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    title = soup.find('div', {'class':'wrap_company'}).find('h2').text
    rate = soup.find('div', {'class':'rate_info'}).find('span', {'class':'blind'}).text

    # get stock quotations
    stock_day = sd.get_sise_day(code)

    stock = {}
    stock['name'] = title
    stock['code'] = code
    stock['rate'] = rate
    stock['sd'] = stock_day
    
    # get stock news
    news_day = news.get_news(code)

    stock['news'] = news_day

    stocks.append(stock)

data = {}

data['name'] = "Stock" 

with open('stock.json', 'w') as f:
    json.dump(data, f, indent = 4)

mn.get_mn()

for code in codes:
    get_stock(code)

# save stocks as json
with open('stock.json', 'r') as f:
    json_data = json.load(f)

json_data['stocks'] = stocks

with open('stock.json', 'w', encoding = 'utf-8') as f:
    json.dump(json_data, f, indent = 4, ensure_ascii = False)