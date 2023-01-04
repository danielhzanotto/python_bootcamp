import requests

MY_LAT = -25.428360,
MY_LON = -49.273251

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]


sunrise_time = sunrise.split("T")[1].split("+")[0]
sunset_time = sunset.split("T")[1].split("+")[0]
print(sunrise_time, sunset_time)
