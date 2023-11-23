from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 設定瀏覽器選項
options = Options()
# 建立 driver
s = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")
chrome = webdriver.Chrome(service=s, options=options)
# 存取 Website
url = "https://www.google.com/"
chrome.get(url)

content = chrome.find_element(By.ID,'APjFqb')
content.send_keys("Selenium Document")
content.send_keys(Keys.RETURN)

# 等待 5 秒鐘以載入頁面
time.sleep(5)
# 關閉瀏覽器視窗
chrome.close()