from flask import Flask,render_template,request
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["PythonMongo"]
user_collections = mydb.users
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/welcome",methods=["GET"])
def welcome():
    return "Welcome, you will see me if you get from me."

@app.route("/user_form",methods=["GET"])
def get_user_form():
    return render_template("user_form.html")
@app.route("/user_form/success",methods=["POST"])
def post_user_form():
    # print(request.form["first_name"])
    # print(request.form["last_name"])
    user_info = {
        "first_name": request.form["first_name"],
        "last_name":request.form["last_name"]
    }
    user_collections.insert_one(user_info)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)