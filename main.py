import requests
from bs4 import BeautifulSoup

import sise_day as sd

code = "005930"
siseURL = "https://finance.naver.com/item/sise.nhn?code="

def get_stock(code):
    result = requests.get(siseURL + code)
    soup = BeautifulSoup(result.text, 'html.parser')
    title = soup.find('div', {'class':'wrap_company'}).find('h2').text
    rate = soup.find('div', {'class':'rate_info'}).find('span', {'class':'blind'}).text

    print(title, rate)

    sd.get_sise_day(code)

get_stock(code)