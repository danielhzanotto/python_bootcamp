import requests
import datetime as dt
import smtplib


MY_LAT = -25.428360
MY_LON = -49.273251

my_email = "mmegaterio@gmail.com"
password = "zkyhcquwdplsxzkj"


def is_night():
    now = dt.datetime.now()
    hour = now.hour
    minute = now.minute

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0
    }
    time_response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    time_response.raise_for_status()
    time_data = time_response.json()

    sunrise = time_data["results"]["sunrise"]
    sunset = time_data["results"]["sunset"]
    sunrise_time = sunrise.split("T")[1].split("+")[0]
    sunrise_hour = int(sunrise_time.split(":")[0])
    sunrise_minute = int(sunrise_time.split(":")[1])
    sunset_time = sunset.split("T")[1].split("+")[0]
    sunset_hour = int(sunset_time.split(":")[0])
    sunset_minute = int(sunset_time.split(":")[1])

    if sunrise_hour > hour > sunset_hour or (hour == sunset_hour and minute > sunset_minute) or (hour == sunrise_hour and minute < sunrise_minute):
        return True


def is_iss_above():
    ISS_response = requests.get("http://api.open-notify.org/iss-now.json")
    ISS_response.raise_for_status()
    latitude = float(ISS_response.json()["iss_position"]["latitude"])
    longitude = float(ISS_response.json()["iss_position"]["longitude"])
    if (MY_LAT - 5) <= latitude <= (MY_LAT + 5) and (MY_LON - 5) <= longitude <= (MY_LON + 5):
        return True


if is_iss_above() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject:ISS ABOVE YOU\n\nISS is currently above you")
