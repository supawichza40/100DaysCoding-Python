class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, searched_flight_data: list):
        self.filtered_flight_data_list = None
        self.available_flight = searched_flight_data

    def filtered_flight_data(self):
        self.filtered_flight_data_list = []
        for data in self.available_flight:
            self.filtered_flight_data_list.append({
                "from": f'{data["cityFrom"]}-{data["flyFrom"]}',
                "to": f"{data['cityTo']}-{data['flyTo']}",
                "price": data["fare"]["adults"],
                "date_from": data["route"][0]["local_arrival"],
                "date_to": data["route"][1]["local_arrival"]
            })

    def get_filtered_flight_data(self):
        return self.filtered_flight_data_list
