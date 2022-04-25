#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager

data_manager = DataManager()
data_manager.update_IATA_code()
data_manager.update_code_to_google_sheet()
