import os

from bs4 import BeautifulSoup
import requests

# user class
from user_log import user_log 


# start script
print('スクリプトを開始します。')

url = "https://www.pixiv.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

user_log.save_html(response)

# tag = soup.select(selector=".logo > a > span")[0]
# print(tag.text)


print('スクリプトを終了します。')
