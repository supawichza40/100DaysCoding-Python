from flask import Flask, render_template, request
from markupsafe import escape
import requests
import sys
import pymongo
from bson import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["PythonDatabase"]
users = mydb.users

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/users/question")
def user():
    return render_template("user_enquiry.html")


@app.route("/users/success", methods=["POST"])
def user_submit():
    print("I am user-submit")
    print(request.form["first_name"],
          request.form["last_name"], file=sys.stderr)
    users.insert_one({
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"]
    })

    return render_template("users.html", first_name=request.form["first_name"])
@app.route("/users")
def get_all_users():
    all_users = users.find()
    print(all_users,file=sys.stderr)
    return render_template("users.html",users=all_users)
    
@app.route("/users/<id>")
def get_user_using_id(id):
    print(id,file=sys.stderr)
    found_user = users.find_one({"_id":ObjectId(id)})
    print(found_user,file=sys.stderr)
    return render_template("detail.html",user=found_user)
    
@app.route("/blog")
def blog():
    blog_response = requests.get(
        url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("posts.html", posts=blog_response.json())


if __name__ == "__main__":
    app.run(debug=True)

# for info in response.json():
#     print(info)
