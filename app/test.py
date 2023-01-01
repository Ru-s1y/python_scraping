# import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
import os

# スクレイピングURL
URL = 'https://www.google.com/'

# コンテナに登録した環境変数の設定
BROWSER_NAME = os.environ['BROWSER_NAME']
HOST_NAME = os.environ['HUB_HOST']

# スクリーンショットの設定
SE_SCREEN_HEIGHT = os.getenv('SE_SCREEN_HEIGHT')
SE_SCREEN_WIDTH  = os.getenv('SE_SCREEN_WIDTH')

# スクリーンショットを保存するためのパスをブラウザごとに指定
BROWSER_FILE_PATH = "screenshot/" + BROWSER_NAME + "/"
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def test_access(driver):
    driver.get(URL)
    driver.save_screenshot('screenshot/' + BROWSER_NAME + '/test.png')
    print(driver.title)
    driver.quit()

if __name__ == '__main__':
    # テスト時のスクリーンショットを保存するためフォルダを作成
    if not os.path.exists(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH)):
        os.makedirs(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH))

    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size='+ SE_SCREEN_WIDTH + ',' + SE_SCREEN_HEIGHT)
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    test_access(driver)
