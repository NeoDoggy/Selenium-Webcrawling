from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
s = Service("./chromedriver-win64/chromedriver-win64/chromedriver.exe")
chrome = webdriver.Chrome(service=s, options=options)
url = "https://www.google.com/"
chrome.get(url)

content = chrome.find_element(By.ID,'APjFqb')
content.send_keys("hahapiyan")
content.send_keys(Keys.RETURN)

time.sleep(5)
chrome.close()
