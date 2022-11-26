#! Программа загружает все комиксы XKCD

import requests, os
from bs4 import BeautifulSoup as bs

url = 'https://xkcd.ru'
# os.makedirs('xkcd', exist_ok=True) # exist_ok=True Если уже есть папка то работает с ней
# i = 5
#
# while not i == 0:
#     # Загрузка страницы.
#     print("Загружается страница %s..." % (url))
#     r = requests.get(url)
#     r.raise_for_status()
#     soup = bs(r.text, 'html.parser')
#
#     # Поиск URL-адреса изображения комикса.
#
#     # data = soup.select('div > a') (*)
#     data = soup.select('a > img')
#
#     if data == []:
#         print('Не удалось найти изображение.')
#     else:
#         # img_url = data[0].img['src'] (*)
#         img_url = data[0].get('src')
#
#         # Загрезка изображения.
#         print('Загрежается изображение %s...' % (img_url))
#         res = requests.get(img_url)
#         res.raise_for_status()
#
#         # Сохранение эелемента в папке ./xkcd
#         image_file = open(os.path.join('xkcd', os.path.basename(img_url)), 'wb')
#         for chunk in res.iter_content(100000):
#             image_file.write(chunk)
#         image_file.close()
#
#     # Получение ссылки кнопи Prev.
#     link = soup.select('.nav a')[1]
#     url = 'https://xkcd.ru' + link.get('href')
#
#     i -= 1
