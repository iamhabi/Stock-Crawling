import requests
from bs4 import BeautifulSoup
import pandas as pd

mainnewsURL = "https://finance.naver.com/news/mainnews.nhn"

result = requests.get(mainnewsURL)
soup = BeautifulSoup(result.text, 'html.parser')

content = soup.find('div', {'class':'mainNewsList'}).find('ul', {'class':'newsList'})

li = content.find_all('li')

def get_mn():
    news = []

    for i in range(len(li)):
        n = []
        if li[i].find('dt', {'class':'articleSubject'}):
            n.append(li[i].find('a').text)
            n.append(li[i].find('a')['href'])
        else:
            n.append(li[i].find('dd').find('a').text)
            n.append(li[i].find('dd').find('a')['href'])

        news.append(n)


    with open('stock.txt', 'w') as f:
        for i in news:
            f.write("%s\n" % i)
        f.write("-----------------------------\n")