import requests
from bs4 import BeautifulSoup

#set url which you want to parse here
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

response = requests.get(url, headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')

keywords = soup.select('.ranking_item > .item_box > .item_title_wrap > .item_title')

for keyword in keywords: print(keyword.text)