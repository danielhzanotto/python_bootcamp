import requests


SHEETY_URL = ""
get_iata_endpoint = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_KEY = ""


class Data:
    def __init__(self):
        pass

    def get_data(self):
        response = requests.get(SHEETY_URL)
        response.raise_for_status()
        return response.json()

    def get_departures(self):
        self.data = self.get_data(self)["prices"]
        self.iata_codes = []
        for i in self.data:
            if len(i["iataCode"]) == 0:
                iata_header = {"apikey": TEQUILA_KEY}
                iata_params = {"term": i["city"]}
                self.iata = self.get_iata(self, iata_params, iata_header)
                self.iata_codes.append(self.iata)
                self.put_iata(i["id"], self.iata)
            else:
                self.iata_codes.append(i["iataCode"])
        return ",".join(self.iata_codes)

    def get_iata(self, parameters, header):
        iata_response = requests.get(
            get_iata_endpoint, params=parameters, headers=header)
        iata_response.raise_for_status()
        return iata_response.json()["locations"][0]["code"]

    def put_iata(id, iata):
        data = {"price": {"iataCode": iata}}
        create_url = f"{SHEETY_URL}/{id}"
        sheet_response = requests.put(create_url, json=data)
        print(sheet_response.text)
        sheet_response.raise_for_status()
