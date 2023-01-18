import requests
from datetime import datetime as dt

API_ID = ""
API_KEY = ""
API_PASSWORD = ""
API_USER = ""
API_TOKEN = ""

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/""

exercises = input()

now = dt.now()
date_today = now.strftime('%Y/%m/%d')
time_now = now.strftime('%H:%M:%S')

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

sheety_header = {"Authorization": "Bearer thisisatokenforthesheetyapi"}

parameters = {
    "query": exercises,
    "gender": "male",
    "weight_kg": 85.2,
    "height_cm": 186.5,
    "age": 28
}


nutri_response = requests.post(
    url=nutritionix_url, headers=header, json=parameters)
nutri_response.raise_for_status()

data = nutri_response.json()


for exercise in data["exercises"]:
    exercise_info = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(
        url=sheety_url, json=exercise_info, headers=sheety_header)
    sheety_response.raise_for_status()
