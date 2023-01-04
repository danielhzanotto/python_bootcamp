import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

iss_position = (latitude, longitude)

print(iss_position)
