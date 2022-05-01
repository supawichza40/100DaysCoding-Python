import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
import os
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_driver_path = "C:\Work\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://connect.treatwell.co.uk/login?route=%2Fcalendar%23venue%2F370180%2Fappointment%2Fday%2F2022-05-01%2F398937")
time.sleep(3)
email_path = driver.find_element(by=By.XPATH,value='//*[@id="login-page"]/div/div[2]/div[1]/form/div[1]/div/div/input')
password_path = driver.find_element(by=By.XPATH,value='//*[@id="login-page"]/div/div[2]/div[1]/form/div[2]/div/div/input')
email_path.send_keys(EMAIL)
password_path.send_keys(PASSWORD)
log_in_btn = driver.find_element(by=By.XPATH,value='//*[@id="login-page"]/div/div[2]/div[1]/form/button')
log_in_btn.click()
time.sleep(3)
booking_one = driver.find_element(by=By.XPATH,value='//*[@id="bcalendar-inst"]/div/div[3]/div/table/tbody/tr[2]/td[4]/div/div[3]')
booking_one.click()
time.sleep(2)
comments = driver.find_elements(by=By.CLASS_NAME,value='appointment--note')
for comment in comments:
    print(comment.text)

print("Done")