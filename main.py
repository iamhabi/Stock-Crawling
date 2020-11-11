import requests
from bs4 import BeautifulSoup

import sise_day as sd
import news
import main_news as mn

codes = ["005930", "000660", "030200", "001040", "051910", "006400", "035720", "035420", "005380", "000150"]
siseURL = "https://finance.naver.com/item/sise.nhn?code="

def get_stock(code):
    result = requests.get(siseURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    title = soup.find('div', {'class':'wrap_company'}).find('h2').text
    rate = soup.find('div', {'class':'rate_info'}).find('span', {'class':'blind'}).text

    with open('stock.txt', 'a') as f:
        f.write(title + "|" + code + " " + rate + "\n")
        f.write("---------------\n")

    sd.get_sise_day(code)
    news.get_news(code)

mn.get_mn()

for code in codes:
    get_stock(code)