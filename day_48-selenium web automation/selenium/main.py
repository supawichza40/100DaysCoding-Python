from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Work\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.amazon.co.uk/Svavo-Dispenser-Automatic-Sanitizer-Container/dp/B07QXS5N3C/?_encoding=UTF8&pd_rd_w=zfeCV&pf_rd_p=822afc68-e2bb-4420-ac6e-1044cd2e7c1d&pf_rd_r=ZHY3STR4D18K7KXMA1GP&pd_rd_r=4d1b25a9-d814-4595-9063-4f6586c1ac56&pd_rd_wg=YEAur&ref_=pd_gw_ci_mcx_mi&th=1")
# price =  driver.find_element(by=By.CSS_SELECTOR,value=".a-price span.a-offscreen+span")
#
# print(price.text.replace("\n","."))
driver.get(url="https://www.python.org/")
event_lists = driver.find_elements(by=By.CSS_SELECTOR,value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li")
event_lists_dict = []
counter = 0
for event in event_lists:
    event_list = event.text.split("\n")
    event_lists_dict.append({
        "time":event_list[0],
        "name":event_list[1]
    })
    # event_lists_dict["time"] = event_list[0]
    # event_lists_dict["name"] = event_list[1]
print(event_lists_dict)


driver.close()