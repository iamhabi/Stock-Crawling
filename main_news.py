import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

mainnewsURL = "https://finance.naver.com/news/mainnews.nhn"

result = requests.get(mainnewsURL)
soup = BeautifulSoup(result.text, 'html.parser')

content = soup.select_one('div.mainNewsList > ul.newsList')

li = content.find_all('li')

def get_mn():
    json_data = {}

    with open('stock.json', 'r') as f:
        json_data = json.load(f)

    json_data['mainnews'] = []

    for i in range(len(li)):
        n = {} 

        if li[i].find('dt', {'class':'articleSubject'}):
            n['title'] = li[i].select_one('a').text
            n['url'] = li[i].select_one('a')['href']
        else:
            n['title'] = li[i].select_one('dd > a').text
            n['url'] = li[i].select_one('dd > a')['href']

        json_data['mainnews'].append(n)

    with open('stock.json', 'w', encoding = 'utf-8') as f:
        json.dump(json_data, f, indent = 4, ensure_ascii = False)