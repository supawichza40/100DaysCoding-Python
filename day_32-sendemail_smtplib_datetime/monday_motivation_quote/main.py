import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import random
load_dotenv()
smtp_mail = "smtp.gmail.com"
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
quote = []
def sending_mail(quote):
    with smtplib.SMTP(smtp_mail) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs="supapython100days@yahoo.com",msg=f"Subject:{quote}\n\n{quote}")
def get_random_quote():
    with open("quotes.txt",mode="r") as reader:
        data = reader.readline()
        while(data!=""):

            quote.append(data)
            data = reader.readline()
get_random_quote()
current_dt = dt.datetime.now()
weekday_num = current_dt.weekday()
if weekday_num ==2:
    sending_mail(random.choice(quote))


