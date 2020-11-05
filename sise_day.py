import requests
from bs4 import BeautifulSoup
import pandas as pd

sisedayURL = "https://finance.naver.com/item/sise_day.nhn?code="

def get_sise_day(code):
    result = requests.get(sisedayURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    table = soup.find('table', {'class':'type2'})

    th = table.find_all('th')

    cate = []

    for i in range(len(th)):
        if i == 2:
            cate.append(th[i].text)
            cate.append('상승/하락')
        else:
            cate.append(th[i].text)

    stock_day = []

    tr = table.find_all('tr', {'onmouseover':'mouseOver(this)'})

    for i in range(len(tr)):
        day = []
        td = tr[i].find_all('td')

        for j in range(len(td)):
            if j == 2:
                day.append(td[j].text.strip())
                day.append(td[j].find('img')['alt'])
            else:
                day.append(td[j].text)
        
        stock_day.append(day)

    print(pd.DataFrame(stock_day, columns = cate))