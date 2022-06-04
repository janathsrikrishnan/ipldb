from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
