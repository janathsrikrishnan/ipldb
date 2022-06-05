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
def player(player_name):
    
    Information = {}
    # need to get details of the player for data base and store in Infomation and pass it 
    return render_template("player.html", player_name = player_name, Information=Information)



# about page of the ipldb
@app.route("/about")
def about():
    
    return render_template("about.html")
