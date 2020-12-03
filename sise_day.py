import requests
from bs4 import BeautifulSoup
import pandas as pd

sisedayURL = "https://finance.naver.com/item/sise_day.nhn?code="
head = ['날짜', '종가', '전일비', '시가', '고가', '저가', '거래량']

def get_sise_day(code):
    result = requests.get(sisedayURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    table = soup.find('table', {'class':'type2'})

    stock_day = []

    tr = table.select('tr')

    for i in range(1, len(tr)):
        day = {}
        td = tr[i].find_all('td')

        if not td[0].text:
            continue

        for j in range(len(td)):
            day[head[j]] = td[j].text.strip()
        
        stock_day.append(day)

    return stock_day