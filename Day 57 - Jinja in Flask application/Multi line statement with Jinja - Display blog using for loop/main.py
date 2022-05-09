from flask import Flask, render_template, request
from markupsafe import escape
import requests
import sys
app = Flask(__name__)
print("Dear")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user/question")
def user():
    return render_template("user_enquiry.html")


@app.route("/user/success", methods=["POST"])
def user_submit():
    print("I am user-submit")
    print(request.form["first_name"],
          request.form["last_name"], file=sys.stderr)

    return render_template("users.html", first_name=request.form["first_name"])


@app.route("/blog")
def blog():
    blog_response = requests.get(
        url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("posts.html", posts=blog_response.json())


if __name__ == "__main__":
    app.run(debug=True)

# for info in response.json():
#     print(info)
