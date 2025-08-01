import requests
from datetime import datetime 

APP_ID = "YOUR APP ID"
API_KEY = "YOUR API KEY"
GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"

nutitionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "YOUR SHEETY LINK"

exercise_text = input("Tell me which exercises you did: ")

today = datetime.now().strftime("%d%m%Y")
current_time = datetime.now().strftime("%X")

headers ={
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
  }
my_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
try:
    response = requests.post(
        url=nutitionix_endpoint,
        json=my_data,
        headers=headers
    )
    response.raise_for_status()
    result = response.json()

except requests.exceptions.HTTPError as err:
    print(f"Nutritionix API Error: {err}")
    print(response.text) 
    exit()

if "exercises" in result and len(result["exercises"]) > 0:
    for exercise in result["exercises"]:
        sheet_inputs = {
            "YOUR SHEET NAME": {
                "date": today,
                "time": current_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        try:
            sheet_response = requests.post(
                url=sheety_endpoint,
                json=sheet_inputs
            )
            sheet_response.raise_for_status()
            print("Sheety Response:", sheet_response.text)
        except requests.exceptions.HTTPError as err:
            print(f"Sheety API Error: {err}")
            print(sheet_response.text)
            print("Please ensure your Google Sheet is shared as 'Anyone with the link can edit'.")
else:
    print("No exercises found or parsed by Nutritionix. Please try a different query.")
