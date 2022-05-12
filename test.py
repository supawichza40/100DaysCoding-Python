import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(user="supavichpython100days@gmail.com",password="Kingza24071997")
server.sendmail()