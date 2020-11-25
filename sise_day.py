import requests
from bs4 import BeautifulSoup
import pandas as pd

sisedayURL = "https://finance.naver.com/item/sise_day.nhn?code="
d = ['날짜', '종가', '전일비', '시가', '고가', '저가', '거래량']

def get_sise_day(code):
    result = requests.get(sisedayURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    table = soup.find('table', {'class':'type2'})

    stock_day = []

    tr = table.find_all('tr', {'onmouseover':'mouseOver(this)'})

    for i in range(len(tr)):
        day = {}
        td = tr[i].find_all('td')

        for j in range(len(td)):
            # day.append(td[j].text.strip())
            day[d[j]] = td[j].text.strip()
        
        stock_day.append(day)

    return stock_day

    # with open('stock.txt', 'a') as f:
    #     f.write("일별시세\n")
    #     for i in stock_day:
    #         f.write("%s\n" % i)
    #     f.write("---------------\n")