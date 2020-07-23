import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.melon.com/chart/index.htm")

print(response)

soup = BeautifulSoup(response.text, 'html.parser')

#main_news = soup.select('#old_content > table > tbody > tr ')

#for data in main_news: print(data.text)

#print(main_news)