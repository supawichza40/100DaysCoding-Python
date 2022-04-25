import requests
SHEETY_API = "https://api.sheety.co/6bf89e618b169825115afd3db08d232d/supavichFlight/prices"
TEQUILA_API_KEY = "NYs2Z9tzLUWJOtTOFfwBGbKOMPs_w7tD"
TEQUILA_LOCATION_END_POINT = "https://tequila-api.kiwi.com/locations/query"
header = {
    "apikey":TEQUILA_API_KEY
}
tequila_location_params = {
    "term":"berlin"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        sheetly_response = requests.get(url=SHEETY_API)
        self.sheetly_flight_data = sheetly_response.json()["prices"]


    def update_IATA_code(self):
        for d in self.sheetly_flight_data:
            tequila_location_params["term"] = d["city"]
            response = requests.get(url=TEQUILA_LOCATION_END_POINT, headers=header, params=tequila_location_params)
            abbr = response.json()["locations"][0]["code"]
            d["iataCode"] = abbr

    def update_code_to_google_sheet(self):
        for d in self.sheetly_flight_data:
            dat = {
                "price": d
            }
            response = requests.put(url=f"{SHEETY_API}/{d['id']}", json=dat)
            print(response.json())
