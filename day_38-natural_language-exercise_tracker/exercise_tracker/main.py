import requests

nutritionix_params = {
    "x-app-id":"f9f33aa7",
    "x-app-key":"a5a1bea66f4425d820b53492377e81c2",
    "x-remote-user-id":"0"
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query":"I walk for 2km and cycling for 5hrs",
    "gender":"male",
    "weight_kg":"90",
    "height_cm":"170",
    "age":"24"
}
nutritionix_response = requests.post(url=exercise_endpoint,headers=nutritionix_params,json=exercise_params)
sheety_api = "https://api.sheety.co/6bf89e618b169825115afd3db08d232d/supavichWorkout/workouts"
response = requests.get(sheety_api)
print(nutritionix_response.json())
print(response.json())
import datetime as dt

for data in nutritionix_response.json()["exercises"]:
    data_params = {
        "workout":{
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": data["name"],
            "duration": data["duration_min"],
            "calories":data["nf_calories"]
        }

    }
    print(data_params)
    response = requests.post(url=sheety_api,json=data_params,headers=nutritionix_params,)
    print(response.text)
