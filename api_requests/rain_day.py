import requests, re
from bs4 import BeautifulSoup as bs

url = 'https://yandex.tm/weather/dashoguz'
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, 'html.parser')
data = soup.find_all('div')

for item in data:
    print(item)