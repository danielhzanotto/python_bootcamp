import requests
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from flight_data import Data

TEQUILA_KEY = ""
search_endpoint = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self):
        self.data = Data

        self.today = datetime.now().strftime('%d/%m/%Y')
        self.six_months = (
            datetime.today() + relativedelta(months=+6)).strftime('%d/%m/%Y')

        self.search_flights()

    def set_parameters(self):
        return {
            "fly_from": "FLN,NVT,CWB",
            "fly_to": self.data.get_departures(self.data),
            "date_from": self.today,
            "date_to": self.six_months,
            "one_for_city": 1,
            "curr": "BRL",
            "locale": "br",
            "nights_in_dst_from": 10,
            "nights_in_dst_to": 30,
            "max_stopovers": 2
        }

    def search_flights(self):
        params = self.set_parameters()
        header = {"apikey": TEQUILA_KEY}
        response = requests.get(url=search_endpoint,
                                params=params, headers=header)
        response.raise_for_status()
        flight_data = response.json()
        self.json_flight = []
        for info in flight_data["data"]:
            self.json_flight.append({
                "cityCodeFrom": info["cityCodeFrom"],
                "cityFrom": info["cityFrom"],
                "cityCodeTo": info["cityCodeTo"],
                "cityTo": info["cityTo"],
                "price": info["price"],
                "local_departure": info["local_departure"].split("T")[0],
                "nightsInDest": info["nightsInDest"],
                "date_return": self.calc_return_data(info["local_departure"], info["nightsInDest"])
            })
        with open("flight_data.json", "w") as f:
            json.dump(self.json_flight, f)

    def calc_return_data(self, departure, nights):
        data = departure.split("T")[0]
        date = data.split("-")
        new_date = datetime(int(date[0]), int(date[1]), int(date[2]))
        return_date = new_date + timedelta(days=nights)
        final_date = return_date.strftime("%Y-%m-%d")
        return str(final_date)
