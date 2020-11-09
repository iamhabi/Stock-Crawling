import requests
from bs4 import BeautifulSoup
import pandas as pd

mainnewsURL = "https://finance.naver.com/news/mainnews.nhn"

result = requests.get(mainnewsURL)
soup = BeautifulSoup(result.text, 'html.parser')

content = soup.find('div', {'class':'mainNewsList'}).find('ul', {'class':'newsList'})

li = content.find_all('li')

news = []

for i in range(len(li)):
    if li[i].find('dt', {'class':'articleSubject'}):
        news.append(li[i].find('a').text)
    else:
        news.append(li[i].find('dd').find('a').text)

# print(pd.DataFrame(news))

with open('mainnews.txt', 'w') as f:
    for i in range(len(news)):
        f.write(news[i] + "\n")