import json
import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
import os
from datetime import datetime

CHROME_DRIVER_PATH = "C:\Work\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.set_window_size(1920,1080)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

obj = driver.find_element(by=By.XPATH,value='//*[@id="productPrice0"]')
print(obj.text)

for index in range(17,-1,-1):
    ob = driver.find_element(by=By.XPATH,value=f'//*[@id="productPrice{}"]')