import requests

nutritionix_params = {
    "x-app-id":"f9f33aa7",
    "x-app-key":"a5a1bea66f4425d820b53492377e81c2",
    "x-remote-user-id":"0"
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_api = "https://api.sheety.co/6bf89e618b169825115afd3db08d232d/supavichWorkout/workouts"
def natural_lang_processing_user_exercise(query):
    exercise_params = {
        "query": query,
        "gender": "male",
        "weight_kg": "90",
        "height_cm": "170",
        "age": "24"
    }
    nutritionix_response = requests.post(url=exercise_endpoint, headers=nutritionix_params, json=exercise_params)
    return nutritionix_response
import datetime as dt
def upload_natural_lang_process_exercise_to_sheet(nutritionix_response):


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

while(True):
    user_answer = input("What exercise have you done today?")
    natur_lang_exercise_list = natural_lang_processing_user_exercise(user_answer)
    upload_natural_lang_process_exercise_to_sheet(natur_lang_exercise_list)

