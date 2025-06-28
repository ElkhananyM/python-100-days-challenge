import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()
NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "Male"
WEIGHT_KG = "80"
HEIGHT_CM = "183"
AGE = 32
SHEETLY_ENDPOINT = os.getenv("SHEETLY_ENDPOINT")
BEARER_AUTH = os.getenv("BEARER_AUTH")

exercises = input("Tell me which exercises you did: ")

params = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=params)
response.raise_for_status()
exercise_stats = response.json()

today = datetime.datetime.now()
date = today.strftime("%x")
time = today.strftime("%X")

sheety_headers = {
    "Authorization": BEARER_AUTH
}

for exercise in exercise_stats["exercises"]:
    sheetly_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_update = requests.post(url=SHEETLY_ENDPOINT, json=sheetly_params, headers=sheety_headers)
    sheet_update.raise_for_status()
    print("Status Code:", sheet_update.status_code)
    print("Response Body:", sheet_update.text)
    # print("Posted:", sheet_update.text)

print(response.text)