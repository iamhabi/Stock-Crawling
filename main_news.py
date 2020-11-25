import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

mainnewsURL = "https://finance.naver.com/news/mainnews.nhn"

result = requests.get(mainnewsURL)
soup = BeautifulSoup(result.text, 'html.parser')

content = soup.find('div', {'class':'mainNewsList'}).find('ul', {'class':'newsList'})

li = content.find_all('li')

def get_mn():
    # news = []

    json_data = {}

    with open('test.json', 'r') as f:
        json_data = json.load(f)

    json_data['mainnews'] = []

    for i in range(len(li)):
        n = {} 
        if li[i].find('dt', {'class':'articleSubject'}):
            # n.append(li[i].find('a').text)
            # n.append(li[i].find('a')['href'])
            n['title'] = li[i].find('a').text
            n['url'] = li[i].find('a')['href']
        else:
            # n.append(li[i].find('dd').find('a').text)
            # n.append(li[i].find('dd').find('a')['href'])
            n['title'] = li[i].find('dd').find('a').text
            n['url'] = li[i].find('dd').find('a')['href']

        json_data['mainnews'].append(n)
        # news.append(n)

    # with open('stock.txt', 'w') as f:
    #     for i in news:
    #         f.write("%s\n" % i)
    #     f.write("-----------------------------\n")

    with open('stock.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent = 4, ensure_ascii = False)