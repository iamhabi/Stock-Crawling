import requests
from bs4 import BeautifulSoup

naverURL = "https://finance.naver.com/item/sise_day.nhn?code="
yahooURL = "https://finance.yahoo.com/quote/"

nhead = ['날짜', '종가', '전일비', '시가', '고가', '저가', '거래량']
yhead = ['Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume']

def get_sise_day_naver(code):
    result = requests.get(naverURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')

    stock_day = []

    tr = soup.select('table.type2 > tr')

    for i in range(1, len(tr)):
        day = {}
        td = tr[i].find_all('td')

        if not td[0].text:
            continue

        for j in range(len(td)):
            day[nhead[j]] = td[j].text.strip()
        
        stock_day.append(day)

    return stock_day

def get_sise_day_yahoo(code):
    result = requests.get(yahooURL + code + "/history?p=" + code)
    soup = BeautifulSoup(result.text, 'html.parser')

    stock_day = []

    tr = soup.select('tbody > tr')

    for i in range(0, 10):
        td = tr[i].select('td')

        day = {}

        for j in range(len(td)):
            day[yhead[j]] = td[j].text.strip()
        
        stock_day.append(day)

    return stock_day