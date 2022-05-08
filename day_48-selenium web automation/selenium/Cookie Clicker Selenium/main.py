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
def get_current_cookies():
    current_cookies_obj = driver.find_element(by=By.CSS_SELECTOR,value='#cookies').text.split(" ")[0].split(",")
    current_cookies_amount = ""
    for num in current_cookies_obj:
        current_cookies_amount+=num

    return int(current_cookies_amount)

start_time =datetime.now()
waiting_limit_second = 5
#productPrice0 - productPrice17
while True:
    if((datetime.now() - start_time).total_seconds()> waiting_limit_second):
        print("inside")
        start_time = datetime.now()
        for index in range(17,-1,-1):
            current_obj = driver.find_element(by=By.XPATH,value=f'//*[@id="productPrice{index}"]')

            if current_obj.text != "":
                if "million" in current_obj.text:
                    num_list = current_obj.text.split(" ")
                    num = float(num_list[0])*1000000
                else:


                    correct_num_format_list = current_obj.text.split(",")
                    num = ""
                    for number in correct_num_format_list:
                        num+=number
                if int(num)<get_current_cookies():
                    obj = driver.find_element(by=By.XPATH,value=f'//*[@id="product{index}"]')
                    obj.click()

    cookies = driver.find_element(by=By.XPATH,value='//*[@id="bigCookie"]')
    cookies.click()
