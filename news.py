import requests
from bs4 import BeautifulSoup

newsURL = "https://finance.naver.com/item/news.nhn?code="
code = "005930"

result = requests.get(newsURL + code)
soup = BeautifulSoup(result.text, 'html.parser')
table = soup.find('table', {'class':'type5'})