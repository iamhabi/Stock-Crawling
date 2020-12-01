import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

ko_sm = ['KOSPI', 'KOSDAQ']
world_sm = ['NAS@IXIC', 'DJI@DJI', 'SPI@SPX']

siURL = 'https://finance.naver.com/sise/sise_index.nhn?code='
sidURL = 'https://finance.naver.com/sise/sise_index_day.nhn?code='
worldURL = 'https://finance.naver.com/world/sise.nhn?symbol='

def get_stock_market():
    json_data = {}

    with open('stock.json', 'r') as f:
        json_data = json.load(f)

    json_data['stock_market'] = []

    for code in ko_sm:
        json_data['stock_market'].append(get_k_stock_market(code))
    
    for code in world_sm:
        json_data['stock_market'].append(get_world_stock_market(code))

    with open('stock.json', 'w', encoding = 'utf-8') as f:
        json.dump(json_data, f, indent = 4, ensure_ascii = False)

def get_k_stock_market(code):
    result = requests.get(siURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.find('h3', {'class':'sub_tlt'}).text
    rate = soup.find('em', {'id':'now_value'}).text

    m = {}
    m['title'] = title
    m['code'] = code
    m['rate'] = rate

    r2 = requests.get(sidURL + code)
    s2 = BeautifulSoup(r2.text, 'html.parser')

    table = s2.find('table', {'class':'type_1'})

    th = table.find_all('th')

    head = []

    for i in range(len(th)):
        head.append(th[i].text)
    
    tr = table.find_all('tr')

    sise_day = []

    for i in range(1, len(tr)):
        td = tr[i].find_all('td')

        if i == 8:
            continue
        elif td[0].text:
            # a = []
            a = {}

            for j in range(len(td)):
                # a.append(td[j].text.strip())
                a[head[j]] = td[j].text.strip()

            sise_day.append(a)

    m['sd'] = sise_day

    return m


def get_world_stock_market(code):
    result = requests.get(worldURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    
    title = soup.find('div', {'class':'h_area'}).find('h2').text
    rate = soup.find('div', {'class':'rate_info'}).find('em').text.strip()

    m = {}
    m['title'] = title
    m['code'] = code
    m['rate'] = rate

    table = soup.find('table', {'id':'dayTable'})

    th = table.find('thead').find_all('th')

    head = []

    for i in range(len(th)):
        head.append(th[i].find('span').text)
    
    tr = table.find('tbody').find_all('tr')

    world_sise_day = []

    for i in range(len(tr)):
        td = tr[i].find_all('td')

        a = {}

        for j in range(len(td)):
            # a.append(td[j].text)
            a[head[j]] = td[j].text
        
        world_sise_day.append(a)
    
    m['sd'] = world_sise_day

    return m