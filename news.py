import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_news_naver(code):
    naverURL = "https://finance.naver.com/item/news_news.nhn?code=" + code + "&page=&sm=title_entity_id.basic&clusterId="

    result = requests.get(naverURL)
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

def get_news_yahoo(code):
    finvizURL = "https://www.finviz.com/quote.ashx?t="

    req = Request(finvizURL + code, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    tr = soup.select('#news-table > tr')

    news = []

    for i in range(0, 10):
        td = tr[i].select('td')

        n = {}

        n['title'] = td[1].select_one('a').text.strip()
        n['date'] = td[0].text.strip()
        n['url'] = td[1].select_one('a')['href']

        news.append(n)

    return(news)