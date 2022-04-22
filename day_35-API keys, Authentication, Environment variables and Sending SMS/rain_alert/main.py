import requests
from twilio.rest import Client
import os

def is_it_rain_12hrs(period: int) -> bool:
    for index in range(period):
        if (hourly_weather[index]["weather"][0]["main"] == "Rain"):
            return True
        else:
            continue
    return False


param = {
    "appid": os.getenv("OWM_API_KEY"),
    "lat": 51.654839,
    "lon": -0.201680,
    "units": "metric"
}
account_sid = 'ACef08d2c54acc66333a64d92dfec4fb87'
auth_token = os.getenv("AUTH_TOKEN")

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=param)
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={param['lat']}&lon={param['lon']}&appid={param['appid']}")
response.raise_for_status()
hourly_weather = response.json()["hourly"]
will_it_rain = is_it_rain_12hrs(12)
if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Today is going to rain, bring your umbrella ☂️",
        from_='+15632782109',
        to='+447377515606'
    )
else:
    print("Today will not rain.")





# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['ACef08d2acc66333a64d92dfec4fb87']#This is use when we set up the environment variable.
# auth_token = os.environ['86fca3ba1e7802a48db10697cb128']#this is use when we set up the environment variable.

