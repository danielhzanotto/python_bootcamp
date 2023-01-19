import requests
from flight_data import Data
import json
from notification_manager import SendEmail


class DataManager:
    def __init__(self):
        self.data = Data.get_data(self)
        self.flights_data = self.get_json()
        self.check_price()

    def get_json(self):
        with open("flight_data.json", "r") as f:
            return json.load(f)

    def check_price(self):
        for city in Data.get_data(self)["prices"]:
            for flight in self.flights_data:
                if city["iataCode"] == flight["cityCodeTo"] and city["lowestPrice"] >= flight["price"]:
                    SendEmail.send_email(self, flight)
