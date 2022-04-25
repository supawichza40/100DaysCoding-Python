import datetime as dt
import requests
from dateutil.relativedelta import *

MY_LOCT = "LON"
today = dt.datetime.now()
three_month_after = today + relativedelta(months=3)
flight_date = today.strftime("%d/%m/%Y")
return_date = three_month_after.strftime("%d/%m/%Y")
TEQUILA_SERVER = "https://tequila-api.kiwi.com/v2/search"
flight_params = {
    "fly_from": MY_LOCT,
    "fly_to": "PAR",
    "date_from": f"{flight_date}",
    "date_to": f"{return_date}",
    "curr": "GBP",
    "max_stopovers": "0",
    "flight_type": "round",
    "nights_in_dst_from": "30",
    "nights_in_dst_to": "60"

}
TEQUILA_API_KEY = "NYs2Z9tzLUWJOtTOFfwBGbKOMPs_w7tD"
header = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.available_flight_list = []

    def search_flight(self):
        for dest in self.flight_data:
            flight_params["fly_to"] = dest["iataCode"]
            response = requests.get(url=TEQUILA_SERVER, headers=header, params=flight_params)
            flight_data = response.json()["data"]
            if flight_data and flight_data[0]["fare"]["adults"] <= dest["lowestPrice"]:
                self.available_flight_list.append(flight_data[0])

    def get_flight_list(self):
        return self.available_flight_list
