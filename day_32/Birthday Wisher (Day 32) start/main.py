import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

print(os.getenv("EMAIL"))
print(os.getenv("PASSWORD"))
connection = smtplib.SMTP("smtp.gmail.com")#this is how to connect to gmail
connection.starttls()#start transport layer security way of securing our connection to email server, prevent someone to intercept and read it and encrypted
