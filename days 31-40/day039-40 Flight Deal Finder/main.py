from data_manager import DataManager
from flight_search import FlightSearch


class Main:
    def __init__(self):

        self.search_flights = FlightSearch()
        self.check_good_prices = DataManager()


Main()
