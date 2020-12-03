import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_news(code):
    newsURL = "https://finance.naver.com/item/news_news.nhn?code=" + code + "&page=&sm=title_entity_id.basic&clusterId="

    result = requests.get(newsURL)
    soup = BeautifulSoup(result.text, 'html.parser')

    tr = soup.select('table.type5 > tbody > tr')

    news = []
    flag = 0

    for i in range(len(tr)):
        n = {} 

        if tr[i].get('class'):
            a = tr[i].get('class')[0]
            if a == "relation_lst":
                flag = 1
            elif a == "hide_news":
                continue
            else:
                n['title'] = tr[i].select_one('a').text
                n['date'] = tr[i].select_one('td.date').text
                n['url'] = tr[i].select_one('a')['href']
        else:
            if flag == 1:
                flag = 0
            else:
                n['title'] = tr[i].select_one('a').text
                n['date'] = tr[i].select_one('td.date').text
                n['url'] = tr[i].find('a')['href']
        
        if n.get('title'):
            news.append(n)

    return news