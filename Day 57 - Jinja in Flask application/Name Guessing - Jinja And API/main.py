from flask import Flask,render_template
from markupsafe import escape
import requests
age_api = "https://api.agify.io/?name="
gender_api = "https://api.genderize.io?name="

app = Flask(__name__)

@app.route("/guess")
def guess_name():
    return "Welcome to Name guessing game"

@app.route("/guess/<name>")
def guess_user_name(name):
    age_response = requests.get(url=age_api+name)
    gender_response = requests.get(url=gender_api+name)
    return render_template("user_guess.html",name=f"{str(name).title()}",gender=gender_response.json()["gender"],age=age_response.json()["age"],amount_people=gender_response.json()["count"])
if __name__ == "__main__":
    app.run(debug=True)