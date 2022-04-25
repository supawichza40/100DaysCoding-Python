#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
data_manager = DataManager()
data_manager.update_IATA_code()
data_manager.update_code_to_google_sheet()
flight_data = data_manager.get_flight_data()

flight_search = FlightSearch(flight_data)
flight_search.search_flight()
available_flight = flight_search.get_flight_list()
flight_data = FlightData(available_flight)
print(flight_data)
flight_data.filtered_flight_data()
result = flight_data.get_filtered_flight_data()
data_manager = DataManager()
notification_manager = NotificationManager(result)
notification_manager.send_flight_data_to_phone()