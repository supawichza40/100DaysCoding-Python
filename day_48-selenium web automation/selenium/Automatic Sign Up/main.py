from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Work\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")
first_name_field = driver.find_element(by=By.NAME,value="fName")
last_name_field = driver.find_element(by=By.NAME,value="lName")
email_field = driver.find_element(by=By.NAME,value="email")

first_name_field.send_keys("Supa")
last_name_field.send_keys("Aussa")
email_field.send_keys("supapython100days@gmail.com")
sign_up_button = driver.find_element(by=By.XPATH,value="/html/body/form/button")
sign_up_button.click()
