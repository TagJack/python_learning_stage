import requests, re, os
from bs4 import BeautifulSoup as bs

# url = 'https://kinogo-net.la/'

# # Loading the page.
# r = requests.get(url)
# r.raise_for_status()
#
# # Creating folder for images.
# os.makedirs('movies_img', exist_ok=True)
# # Getting the data
# soup = bs(r.text, 'html.parser')
# data = soup.find_all('a', class_='carou img-box')
#
# list = []
# for item in data:
#     # getting url of the image.
#     img_url = 'https://kinogo-net.la' + item.img['data-src']
#     # Loading the image.
#     img = requests.get(img_url)
#     file = open(os.path.join('movies_img', os.path.basename(img_url)), 'wb')
#     for chunk in img.iter_content(100000):
#         file.write(chunk)
#     file.close()
#     # Printing stuff
#     print(img_url)
#     print(item['title'])
#     print(item.getText().strip())
#     print(item['href'])
#     print("*"*9+"\n")

#
url = 'https://kinogo-net.la'

res = requests.get(url)
res.raise_for_status()

os.makedirs('movie_pics', exist_ok=True)

soup = bs(res.text, 'html.parser')
data = soup.select('a.kino-img img-box')

print(len(data))




# url = 'https://kinogo-net.la/'
# res = requests.get(url)
# res.raise_for_status()
#
# soup = bs(res.text, 'html.parser')
# data = soup.select('div.msupdate_block_list_item_inner')
#
# resp = input("Enter the name or enter 'a' to see all update.\n: ")
# # what need.
# if len(resp) > 1:
#     for item in data:
#         info = ''.join(re.sub(r'(\s)(\s+)', r'\1', item.getText()))
#         if resp.title() in info:
#             print("*"*10)
#             print(info)
#             print("*"*10)
# else:
#     # all updates.
#     for item in data:
#         print(''.join(re.sub(r'(\s)(\s+)', r'\1', item.getText())))
#         print('*'*10)