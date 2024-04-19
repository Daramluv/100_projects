import requests
from datetime import datetime

APP_ID = "2fbd7197"
API_KEY = "4e47fee644b59df9bb2c08703dd089cf"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint ="https://api.sheety.co/d652a027fee5e1a53469a45ec699a8f8/workoutTracking/workouts"
exercise_text = input("Tell me which excercises you did: ")

#Your personal data. Used by Nutritionix to calculate calories
GENDER = "female"
WEIGHT_KG = "50"
HEIGHT_CM = "157"
AGE = 30


# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.get(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "workout"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
        "date": today_date,
        "time": now_time,
        "exercise":exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
    }
    
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)