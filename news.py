import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_news(code):
    newsURL = "https://finance.naver.com/item/news_news.nhn?code=" + code + "&page=&sm=title_entity_id.basic&clusterId="

    result = requests.get(newsURL)
    soup = BeautifulSoup(result.text, 'html.parser')
    table = soup.find('table', {'class':'type5'}).find('tbody')

    tr = table.find_all('tr')

    news = []
    flag = 0

    for i in range(len(tr)):
        n = []

        if tr[i].get('class'):
            a = tr[i].get('class')[0]
            if a == "relation_lst":
                flag = 1
            elif a == "hide_news":
                continue
            else:
                print(tr[i].find('a').text)
        else:
            if flag == 1:
                flag = 0
            else:
                print(tr[i].find('a').text)
        
        print(flag)
        
        # n.append(tr[i].find('a').text)
        # n.append(tr[i].find('td', {'class':'info'}).text)
        # n.append(tr[i].find('td', {'class':'date'}).text)
        # n.append(tr[i].find('a').get('href'))

    #     news.append(n)

    # print(pd.DataFrame(news))

get_news("000660")