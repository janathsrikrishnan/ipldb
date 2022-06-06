from flask import Flask
from flask import render_template
from flask import g

from get_connection import  Connection

app = Flask(__name__, template_folder="template")

@app.before_request
def connection():
    g.conn = Connection()

# index page of the ipldb
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pointTable/<int:year>")
def pointTable(year : int):
    
    # get the connection to the database
    cur = g.conn.cursor()
    cur.execute(f"SELECT * FROM pointTable WHERE editionNo = {year}")
    # storing recordes as list
    pointtable = cur.fetchall()
    # pass the year and list to render the html page
    return render_template("pointTable.html", year=year, pointtable=pointtable)

# player info page
@app.route("/player/<player_name>")
def player(player_name : str):
    
    Information = {}
    # need to get details of the player for data base and store in Infomation and pass it 
    return render_template("player.html", player_name = player_name, Information=Information)

@app.route("/seasons/<int:year>")
def seasons(year : int):
    cur = g.conn.cursor()
    cur.execute(f"SELECT * FROM seasonStats WHERE editionNo = {year}")
    # storing recordes as list
    data = cur.fetchall()
    return render_template("seasons.html", data=data, year=year)

@app.route("/trail")
def trail():
    return render_template("trail.html")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("error.html", error_code=404), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html", error_code=500), 500

# about page of the ipldb
@app.route("/about")
def about():
    
    return render_template("about.html")
