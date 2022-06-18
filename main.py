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
    teamLabel = [team[1] for team in pointtable]
    points = [points[10] for points in pointtable]
    nrr = [float(nrr[7]) for nrr in pointtable]
    # pass the year and list to render the html page
    return render_template("pointTable.html", year=year, pointtable=pointtable, teamLabel=teamLabel, points=points, nrr=nrr)

# player info page
@app.route("/Teams/<int:year>")
def Teams(year : int):
    cur = g.conn.cursor()
    cur.execute(f"SELECT teamname FROM seasonstats WHERE editionno = {year} ")
    teams = cur.fetchall()
    # need to get details of the player for data base and store in Infomation and pass it 
    return render_template("Teams.html", teams=teams, year=year)

@app.route("/teams/<teamName>/<int:year>")
def players(teamName : str, year : int):
    cur = g.conn.cursor()
    team = teamName.replace(" ", "-").lower()
    print(team)
    cur.execute(f"SELECT playerName, photo, role FROM players WHERE editionNo={year} AND teamname='{team}'")
    players = cur.fetchall()
    return render_template("players.html", players=players, year=year, teamName=teamName)

@app.route("/team/<teamName>/<int:year>/<playerName>")
def player(teamName: str, year : int, playerName : str):
    cur = g.conn.cursor()
    print(playerName)
    team = teamName.replace(' ', '-').lower()
    cur.execute(f"SELECT * FROM players WHERE editionNo={year} AND teamname='{team}' AND playername='{playerName.strip()}'")
    Information = cur.fetchone()
    cur.execute(f"SELECT teamname, editionno FROM players WHERE playername='{playerName.strip()}'")
    teams = cur.fetchall()
    return render_template("player.html", Information=Information, teamnames = teams, playerName=playerName)

@app.route("/team/<teamName>/<int:year>/<int:playerId>")
def playerID(teamName: str, year : int, playerId : int):
    cur = g.conn.cursor()
    team = teamName.replace(" ", "-").lower()
    cur.execute(f"SELECT * FROM players WHERE editionno={year} AND playerid={playerId}")
    
    Information = cur.fetchone()
    try:
        playerName = Information[3]
    except:
        playerName = "Unkown"
    cur.execute(f"SELECT teamname, editionno FROM players WHERE playername='{playerName.strip()}'")
    teams = cur.fetchall()
    return render_template("player.html", Information=Information, teamnames = teams, playerName=playerName)


@app.route("/seasons/<int:year>")
def seasons(year : int):
    cur = g.conn.cursor()
    cur.execute(f"SELECT * FROM seasonStats WHERE editionNo = {year}")
    # storing recordes as list
    data = cur.fetchall()
    return render_template("seasons.html", data=data, year=year)

@app.route("/matches/<int:year>")
def matches(year : int):
    coll = g.conn.cursor()
    coll.execute(f"SELECT matchdate, firstbatting, secondbatting, commentss, firstsummary, secondsummary FROM matchs WHERE editionNo={year} ")
    orderPresent = False
    comment = True
    match = coll.fetchall()
    return render_template("match.html", match=match, year=year, orderPresent=orderPresent, comment=comment)

@app.route("/stats/<int:year>")
def stats(year : int):
    coll = g.conn.cursor()
    coll.execute(f"SELECT playername, wickets, bestbowledinnings, teamname FROM purplecap WHERE editionno={year}")
    purplecap = coll.fetchall()
    coll.execute(f"SELECT playername, runs, highestscore, teamname, playerid FROM orangecap WHERE editionno = {year}")
    orangecap = coll.fetchall()
    return render_template('stats.html', purplecap=purplecap, orangecap=orangecap, year=year)

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
