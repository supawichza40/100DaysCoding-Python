import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By

chrome_driver_path = "C:\Work\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://stackoverflow.com/")

log_in_button = driver.find_element(by=By.LINK_TEXT,value="Log in")
log_in_button.click()
time.sleep(2)
log_in_with_google_btn = driver.find_element(by=By.XPATH,value='//*[@id="openid-buttons"]/button[1]')
log_in_with_google_btn.click()
time.sleep(2)
