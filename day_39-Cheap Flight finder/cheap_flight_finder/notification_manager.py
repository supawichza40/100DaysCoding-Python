import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ACef08d2c54acc66333a64d92dfec4fb87"
TWILIO_AUTH_TOKEN = "86fca3ba1eb5f7802a48db10697cb128"
TWILIO_PHONE_NUM = "+15632782109"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, filtered_flight_data):
        self.filtered_flight_data = filtered_flight_data

    def send_flight_data_to_phone(self):
        if self.filtered_flight_data:
            for data in self.filtered_flight_data:
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

                message = client.messages.create(
                    body=f'Low price alert!Only £{data["price"]} to fly from {data["from"]} to {data["to"]}, from{data["date_from"]} to {data["date_to"]}',
                    from_=TWILIO_PHONE_NUM,
                    to='+447377515606'
                )

                print(message.sid)
