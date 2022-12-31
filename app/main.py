import os

from bs4 import BeautifulSoup
import requests

# user class
from user_log import user_log 


# start script
print('スクリプトを開始します。')

url = os.getenv('SCRAPING_URL') or "https://google.co.jp/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

user_log.save(response)

# tag = soup.select(selector=".logo > a > span")[0]
# print(tag.text)


print('スクリプトを終了します。')
