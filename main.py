from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder="template")


# index page of the ipldb
@app.route("/")
def home():
    return render_template("index.html")

# player info page
@app.route("/player/<player_name>")
def player(player_name):
    Information = {}
    # need to get details of the player for data base and store in Infomation and pass it 
    return render_template("player.html", player_name = player_name, Information=Information)



# about page of the ipldb
@app.route("/about")
def about():
    return render_template("about.html")
