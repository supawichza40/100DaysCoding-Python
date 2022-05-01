from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Work\Development\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)
#Get number of article from wikipedia
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(by=By.CSS_SELECTOR,value="#articlecount a")
print(article_count.text)

driver.close()
