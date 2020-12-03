import json
import requests
from bs4 import BeautifulSoup

ko_sm = ['KOSPI', 'KOSDAQ']
world_sm = ['NAS@IXIC', 'DJI@DJI', 'SPI@SPX']

siURL = 'https://finance.naver.com/sise/sise_index.nhn?code='
sidURL = 'https://finance.naver.com/sise/sise_index_day.nhn?code='
worldURL = 'https://finance.naver.com/world/sise.nhn?symbol='

head = ['날짜', '종가', '전일비', '시가', '고가', '저가']

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

    title = soup.select_one('h3.sub_tlt').text
    rate = soup.select_one('em#now_value').text

    m = {}
    m['title'] = title
    m['code'] = code
    m['rate'] = rate

    r2 = requests.get(sidURL + code)
    s2 = BeautifulSoup(r2.text, 'html.parser')

    tr = s2.select('table.type_1 > tr')

    # print(tr)

    sise_day = []

    for i in range(2, 5):
        td = tr[i].select('td')

        a = {}

        for j in range(len(td)):
            a[head[j]] = td[j].text.strip()

        sise_day.append(a)

    tr = tr[8].select('tr')[:3]

    for i in range(len(tr)):
        td = tr[i].select('td')

        a = {}

        for j in range(len(td)):
            a[head[j]] = td[j].text.strip()

        sise_day.append(a)

    m['sd'] = sise_day

    return m

def get_world_stock_market(code):
    result = requests.get(worldURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    
    title = soup.select_one('div.h_area > h2').text
    rate = soup.select_one('div.rate_info > div.today > p > em').text.strip()

    m = {}
    m['title'] = title
    m['code'] = code
    m['rate'] = rate

    tr = soup.select('table#dayTable > tbody > tr')

    world_sise_day = []

    for i in range(len(tr)):
        td = tr[i].select('td')

        a = {}

        for j in range(len(td)):
            a[head[j]] = td[j].text
        
        world_sise_day.append(a)
    
    m['sd'] = world_sise_day

    return m