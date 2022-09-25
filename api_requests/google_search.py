import requests, re, sys, pyperclip, webbrowser
from bs4 import BeautifulSoup as bs

if len(sys.argv) > 1:
    # Takes what's written.
    adress = sys.argv[1:]
    # Takes what in clickboard.
else:
    adress = pyperclip.paste()

resp = input("Enter 'y' if you want to open web-sites. \nEnter 'n' if only result of search.\n: ")
if resp == 'n':
    webbrowser.open('https://www.google.com/search?q='+''.join(adress).replace(' ', '+'))
else:
    # The URL.
    url = 'https://www.google.com/search?q='+''.join(adress).replace(' ', '+')

    # Loading the page
    r = requests.get(url)
    r.raise_for_status()
    soup = bs(r.text, 'html.parser')

    # Getting the data.
    data = soup.select('div > a')
    result_list = []
    # Listing links.

    for link in data:
        # result link are in elements that have h3 elements within.
        if 'h3' in str(link):
            result_list.append(link.get('href'))

    # We don't want to open all of the links.
    num_open = min(3, len(result_list))
    # Formatting and opening.
    for i in range(num_open):
        url = ''.join(re.findall(r"(?<==).+(?=&sa)", result_list[i])) # I know, but i cannot make it without re.
        webbrowser.open(url)