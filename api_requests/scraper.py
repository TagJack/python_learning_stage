#! Gets news.
from bs4 import BeautifulSoup as bs
import requests

# Loading page
URL = 'https://turkmenportal.com/'
r = requests.get(URL)

# Getting data.
soap = bs(r.text, "html.parser")
links = soap.find_all('div', class_="entry-title")
for one in links:
    try:
        print(one.a.getText().lstrip()) # Title.
        print(one.time.getText().lstrip()) # Time.
        print(one.a['href']) # Link
        print() # Space

    except AttributeError: # There was this exp.
        pass
