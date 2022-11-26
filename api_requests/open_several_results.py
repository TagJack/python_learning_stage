from bs4 import BeautifulSoup as bs
import re, webbrowser, requests

print("Googling...")
# url = 'https://www.google.com/search?q=kino&client=firefox-b-d&sxsrf=ALiCzsYeIT7RQ7oN3Ct19z4PVTZCtxCKmw%3A1662960142041&ei=DsIeY_yWAormkgWA85CIDw&ved=0ahUKEwj81aqkwY76AhUKs6QKHYA5BPEQ4dUDCA0&uact=5&oq=kino&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCggAELEDEIMBEAoyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQM6DQgAEEcQ1gQQsAMQyQM6CggAEEcQ1gQQsAM6BwgAELADEEM6DAguEMgDELADEEMYAToHCCMQ6gIQJzoICAAQsQMQgwE6CwguEIAEELEDEIMBOgoIABCABBBGEP0BOgwILhCABBDUAhAKEAE6CQgAEIAEEAoQAToFCAAQgARKBQg8EgE2SgQIQRgASgQIRhgAUIQXWJysAWDprgFoCnABeAiAAckdiAH3nAGSAQkxLjYtNi45LTSYAQCgAQGwAQrIAQrAAQHaAQQIARgI&sclient=gws-wiz'
# # Loading the page.
# res = requests.get(url)
# res.raise_for_status()
#
# # Find and get the data.
# soup = bs(res.text, 'html.parser')
# data = soup.select('div > a')
#
# # if there are needed links they get in list.
# data_fmt = []
# for i in data:
#     if 'h3' in str(i):
#         data_fmt.append(i)
#
# # We want to open couple of them not all so...
# numOpen = min(4, len(data_fmt))
# for item in range(numOpen):
#     url = data_fmt[item]['href']
#     # It won't work without formatting.
#     url_fmt = ''.join(re.findall(r'(?<==).*', url))
#     webbrowser.open(str(url_fmt))


