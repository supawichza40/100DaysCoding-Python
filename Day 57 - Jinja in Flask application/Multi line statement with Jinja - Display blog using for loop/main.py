from flask import Flask,render_template
from markupsafe import escape
import requests

app = Flask(__name__)
print("Dear")
@app.route("/blog")
def blog():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("posts.html",posts=blog_response.json())
if __name__ == "__main__":
    app.run(debug=True)

# for info in response.json():
#     print(info)