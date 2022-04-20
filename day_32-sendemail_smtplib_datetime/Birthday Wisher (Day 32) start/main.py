import smtplib
import socket

from dotenv import load_dotenv
import os
load_dotenv()
#this is how to call a variable.
print(os.getenv("EMAIL"))
print(os.getenv("PASSWORD"))
try:
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    recipient_email = "supapython100days@yahoo.com"
    connection = smtplib.SMTP("smtp.gmail.com")#this is how to connect to gmail
    connection.starttls()#start transport layer security way of securing our connection to email server, prevent someone to intercept and read it and encrypted
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs=recipient_email,msg="Subject:Hello\n\nThis is a content of my email")
    connection.close()#we have to close connection after finish
except AttributeError as error:
    print("Invalid email or password, please check that both is valid.")
except socket.gaierror as error:
    print("Socket error, please check your SMTP path is correct for specific provider.")