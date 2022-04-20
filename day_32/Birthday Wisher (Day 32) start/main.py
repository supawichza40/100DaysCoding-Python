import smtplib
from password import my_email,password
my_email = "supapython100days@gmail.com"
password = "Kingza40"
connection = smtplib.SMTP("smtp.gmail.com")#this is how to connect to gmail
connection.starttls()#start transport layer security way of securing our connection to email server, prevent someone to intercept and read it and encrypted
connection.login(user=my_email,password="Kingza40")
