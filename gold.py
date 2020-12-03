import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

goldURL = "https://finance.naver.com/marketindex/goldDetail.nhn"
dailyURL = "https://finance.naver.com/marketindex/goldDailyQuote.nhn"

head = ['날짜', '매매기준율', '전일대비']

def get_gold():
    result = requests.get(goldURL)
    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.select_one('h2').text.strip()
    rate = soup.select_one('p.no_today > em').text.strip()

    gold = {}

    gold['title'] = title
    gold['rate'] = rate

    r2 = requests.get(dailyURL)
    s2 = BeautifulSoup(r2.text, 'html.parser')

    # tr = s2.find('table').find('tbody').find_all('tr')
    tr = s2.select('table > tbody > tr')

    daily = [] 

    for i in range(len(tr)):
        td = tr[i].select('td')

        g = {}

        for j in range(0, 3):
            g[head[j]] = td[j].text.strip()

        daily.append(g)
    
    gold['daily'] = daily

    json_data = []

    with open('stock.json', 'r') as f:
        json_data = json.load(f)
    json_data['gold'] = gold
    
    with open('stock.json', 'w', encoding = 'utf-8') as f:
        json.dump(json_data, f, indent = 4, ensure_ascii = False)