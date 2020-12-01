import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

erURL = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_"
dailyURL = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_"

country = ['USDKRW', 'EURKRW', 'JPYKRW']
head = ['날짜', '매매기준율', '전일대비']

def get_er():
    json_data = []

    with open('stock.json', 'r') as f:
        json_data = json.load(f)

    json_data['exchange_rate'] = []

    for c in country:
        json_data['exchange_rate'].append(get_exchange_rate(c))

    with open('stock.json', 'w', encoding = 'utf-8') as f:
        json.dump(json_data, f, indent = 4, ensure_ascii = False)

def get_exchange_rate(country):
    er = {}

    result = requests.get(erURL + country)
    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.find('h2').text.strip()
    rate = soup.find('div', {'id':'content'}).find('p').find('em').text.strip()

    er['title'] = title
    er['rate'] = rate

    r2 = requests.get(dailyURL + country)
    s2 = BeautifulSoup(r2.text, 'html.parser')

    table = s2.find('table', {'class':'tbl_exchange'})
    tr = table.find('tbody').find_all('tr')

    daily = []

    for i in range(len(tr)):
        td = tr[i].find_all('td')

        a = {}

        for j in range(0, 3):
            a[head[j]] = td[j].text.strip()
        
        daily.append(a)
    
    er['daily'] = daily

    return er