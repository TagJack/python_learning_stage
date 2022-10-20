import requests, re, os
from bs4 import BeautifulSoup as bs

url = 'https://kinogo-net.la/'

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
# updates.
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, 'html.parser')
data = soup.select('.msupdate_block_list_item_inner')
print(len(data))
for item in data:
    # print(item.a['href'])
    # print(item.img['alt'])
    print(str(item.div()))
    print('*'*10)


