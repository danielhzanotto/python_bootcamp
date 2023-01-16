import requests
from datetime import datetime as dt


USERNAME = "megateriomega"
TOKEN = "alteredkey"
ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
today = dt.now().strftime("%Y%m%d")

headers = {"X-USER-TOKEN": TOKEN}

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}


data_post = {"date": today, "quantity": "8"}
data_put = {"quantity": "7"}

# CREATE ACCOUNT
# response = requests.post(url=PIXELA_ENDPOINT, json=parameters)
# print(response.text)

# CREATE GRAPH
# response = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", json=graph_config, headers=headers)

# POST DATA
# response = requests.post(url=f"{graph_endpoint}/{ID}", json=data_post, headers=headers)

# UPDATE DATA
# response = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}", json=data_put, headers=headers)

# DELETE DATA
# response = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}", headers=headers)
