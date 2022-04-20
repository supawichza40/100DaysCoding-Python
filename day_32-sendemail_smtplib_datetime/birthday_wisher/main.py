##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import random
import smtplib
from dotenv import load_dotenv
import pandas
import datetime as dt
import os
load_dotenv()
data = pandas.read_csv("birthdays.csv")
dict_result = {(d["day"],d["month"]):d for index,d in data.iterrows()}
today = dt.datetime.now()
day = today.day
month = today.month

if (day,month) in dict_result:
    name = dict_result[(day,month)]["name"]
    email = dict_result[(day,month)]["email"]
    random_letter = random.randint(1,3)
    wish = ""
    with open(file=f"letter_templates/letter_{random_letter}.txt",mode="r") as reader:
        wish = reader.read()
    named_letter = wish.replace("[NAME]",name)
    print(os.getenv("EMAIL"),os.getenv("PASSWORD"))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("EMAIL"),password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr=os.getenv("EMAIL"),to_addrs=email,msg=f"Subject: Happy Birth Day {name}\n\n{named_letter}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




