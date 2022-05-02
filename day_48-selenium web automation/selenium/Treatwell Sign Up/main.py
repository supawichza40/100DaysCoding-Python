import json
import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
import os
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
today_staff = {}
chrome_driver_path = "C:\Work\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://connect.treatwell.co.uk/login?route=%2Fcalendar%23venue%2F370180%2Fappointment%2Fday%2F2022-05-01%2F398937")
time.sleep(2)
email_path = driver.find_element(by=By.XPATH,value='//*[@id="login-page"]/div/div[2]/div[1]/form/div[1]/div/div/input')
password_path = driver.find_element(by=By.XPATH,value='//*[@id="login-page"]/div/div[2]/div[1]/form/div[2]/div/div/input')
email_path.send_keys(EMAIL)
password_path.send_keys(PASSWORD)
log_in_btn = driver.find_element(by=By.XPATH,value='//*[@id="login-page"]/div/div[2]/div[1]/form/button')
log_in_btn.click()
time.sleep(5)
# booking_one = driver.find_element(by=By.XPATH,value='//*[@id="bcalendar-inst"]/div/div[3]/div/table/tbody/tr[2]/td[4]/div/div[3]')
# booking_one.click()
# time.sleep(2)
comments = driver.find_elements(by=By.CLASS_NAME,value='appointment--note')
# for comment in comments:
#     print(comment.text)
def get_date_from_treatwell():
    date = driver.find_element(by=By.XPATH,value='//*[@id="calendar-holder"]/div[2]/div[1]/div[1]/div[3]/div/ul/li[2]/span')
    today_staff["date"] = date.text
def get_staff_names_from_treatwell():
    staff_name_lists = driver.find_elements(by=By.XPATH,value='//*[@id="bcalendar-inst"]/div/div[1]/table/tbody/tr/td')
    for staff in staff_name_lists:
        class_name = staff.get_attribute("class")
        if staff.text != ' ':
            if staff.text != '':
                index = int(class_name.split(" ")[1].split("-")[2])
                staff_name = staff.text.split("\n")[1]
                today_staff[f"{index}"] = {
                    "name" : staff_name,
                    "bookings":[]
                }

staffs_booking_lists = driver.find_elements(by=By.XPATH,value='//*[@id="bcalendar-inst"]/div/div[2]/div/table/tbody/tr[2]/td')
counter = 0
get_date_from_treatwell()
get_staff_names_from_treatwell()
for staff_col in staffs_booking_lists:

    bookings = staff_col.find_elements(by=By.CLASS_NAME,value='wc-cal-event')
    if bookings!=[]:
        print(bookings)
        for booking in bookings:
            if booking.text != "":
                customer_booking_data_list = booking.text.split("\n")
                customer_booking_dict = {
                    "time":customer_booking_data_list[0],
                    "customer_name":customer_booking_data_list[1],
                    # "massage_type":customer_booking_data_list[2],
                    # "duration":customer_booking_data_list[3]
                }
                if customer_booking_data_list[1] == "dear":
                    print("Yes")
                booking.click()
                time.sleep(2)
                customer_pop_up_treatments_lists = driver.find_elements(by=By.XPATH,value='//*[@id="react-root"]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]/div[1]/div')
                for treatment in customer_pop_up_treatments_lists:
                    name = treatment.find_element(by=By.CSS_SELECTOR,value='form > div.appointment--item--content.clearfix > div.js-appointment-data-rows > div > div.appointment--content--item.float.for-max-select.js-employee.right > div > div > div.InputBorder--container--3f2d33 > div > div > div > div')
                    if today_staff[f'{counter}']["name"] in name.text:
                        treatment_type = treatment.find_element(by=By.CSS_SELECTOR,value='form > div.appointment--item--content.clearfix > div.appointment--content--item')

                        # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div > form > div.appointment--item--content.clearfix > div.appointment--content--item > div.js-offerId.is-react > div > div.InputBorder--container--3f2d33 > div > div > div > div
                        # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div > form > div.appointment--item--content.clearfix > div.appointment--content--item > div.js-offerId > div > div
                        # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div > form > div.appointment--item--content.clearfix > div.appointment--content--item > div.js-skuId.extra-top-margin.is-react > div
                        price = treatment.find_element(by=By.CSS_SELECTOR,value='form > div.appointment--item--footer.clearfix > span > span')
                        note_container = treatment.find_element(by=By.CSS_SELECTOR, value='form > div.js-notes.textarea-container')
                        customer_booking_dict["note"] = note_container.text
                        customer_booking_dict["price"] = price.text
                        customer_booking_dict["treatment"] = treatment_type.text.split("\n")[0]
                        try:
                            duration_obj = treatment.find_element(by=By.CSS_SELECTOR,value='form > div.appointment--item--content.clearfix > div.appointment--content--item > div.js-skuId.extra-top-margin.is-react > div')
                            customer_booking_dict["duration"] = duration_obj.text
                        except:
                            customer_booking_dict["duration"] = "Invalid"
                        print(f'This is {name.text}')
                close_pop_up_btn = driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div/div[2]/div/div/span')
                close_pop_up_btn.click()
                today_staff[f'{counter}']['bookings'].append(customer_booking_dict)
                print(today_staff)
                time.sleep(2)
                    # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div:nth-child(2) > form > div.appointment--item--content.clearfix > div.js-appointment-data-rows > div > div.appointment--content--item.float.for-max-select.js-employee.right > div > div > div.InputBorder--container--3f2d33 > div > div > div > div
                    # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div:nth-child(1) > form > div.appointment--item--content.clearfix > div.js-appointment-data-rows > div > div.appointment--content--item.float.for-max-select.js-employee.right > div > div > div.InputBorder--container--3f2d33 > div > div > div > div
                    # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div:nth-child(1) > form > div.appointment--item--footer.clearfix > span > span
                    # react-root > div > div > div > div.ui-dialog.dialog2.react-dialog.calendar-item-editor.top > div > div > div:nth-child(3) > div > div > div.content-scroll > div.js-appointments.udv-appointments > div:nth-child(2) > form > div.js-notes.textarea-container > textarea



    counter+=1
with open(f"{today_staff['date']}.json","w") as data_file:
    json.dump(today_staff,data_file,indent=4)
# print(today_staff)
print("Done")

# driver.close()