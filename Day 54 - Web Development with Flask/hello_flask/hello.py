from flask import Flask
from test import print_something

from flask import Flask,render_template
import os
template_folder = './testing_templates'
app = Flask(__name__,template_folder=template_folder)
@app.route("/")
def hello_world():
    return render_template("hello.html")#There is a default setting for setting path to templates, and it look at that page for html.


if __name__ == "__main__":
    app.run()
