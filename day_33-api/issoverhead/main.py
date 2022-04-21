import math
import smtplib
import time

import requests
from datetime import datetime

EMAIL = "supapython100days@gmail.com"
PASSWORD = "Kingza40"
MY_LAT = 51.656434  # Your latitude
MY_LONG = -0.201567  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
utc = datetime.utcnow()
utc_hr = int(str(utc).split(" ")[1].split(":")[0])

def is_possible_to_view_iss():
    if math.floor(MY_LAT)-5<iss_latitude<math.ceil(MY_LAT)+5 and math.floor(MY_LONG)-5<iss_longitude<math.ceil(MY_LONG)+5 and utc_hr <= sunrise or utc_hr >= sunset:
        return True
    else:
        return False
#If the ISS is close to my current position
# and it is currently dark
while(True):
    if is_possible_to_view_iss():
        print("possible")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f"Subject: ISS is over your head\n\n Look up the sky and spot the ISS International Space Station")
    else:
        print("Not possible")
    time.sleep(60)




