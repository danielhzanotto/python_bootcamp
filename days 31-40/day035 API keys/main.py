import requests
import json
import smtplib


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "sdfdfgzdfbvdzbvf "

my_email = "mmegaterio@gmail.com"
password = "zkyhcquwdplsxzkj"

parameters = {
    "lat": -27.594870,
    "lon": -48.548222,
    "appid": API_KEY,
}

data = requests.get(OWM_Endpoint, params=parameters)
data.raise_for_status()


weather_data = data.json()

weather_forecast = [{
    "date": time["dt_txt"],
    "temp": float(time["main"]["temp"]) - 273.15,
    "code": time["weather"][0]["description"],
    "humidity": time["main"]["humidity"],
    "wind_speed": time["wind"]["speed"],
} for time in weather_data["list"]]

with open("data.json", "w") as file:
    json.dump(weather_forecast, file, indent=4)


print()


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="Subject:ISS ABOVE YOU\n\nISS is currently above you")
