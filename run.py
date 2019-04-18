from app import app
from db import db
from flask import Flask, render_template
import requests

db.init_app(app)

# before the first request runs, it's going to create the database:
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template("home.html")




numCarsEast = None
numCarsWest = None
numCarsSouth = None
numCarsNorth = None


@app.route('/info.json', methods=['GET', 'POST'])
def getInfo():
    if  requests.method == 'GET':
        lightEast = {}
        lightWest = {}
        lightNorth = {}
        lightSouth = {}
        intersection1 = {}
        lightEast['cars'] = numCarsEast
        lightWest['cars'] = numCarsWest
        lightNorth['cars'] = numCarsNorth
        lightSouth['cars'] = numCarsSouth
        intersection1['eastLight'] = lightEast
        intersection1['westLight'] = lightWest
        intersection1['northLight'] = lightNorth
        intersection1['southLight'] = lightSouth
        return jsonify(intersection=intersection1)

@app.route('/cars', methods=['GET', 'POST'])
def cars():
    global numCarsEast, numCarsWest, numCarsSouth, numCarsNorth
    if requests.method == 'POST':
        numCarsEast = requests.form.get('eastLightInt1', None)
        numCarsWest = requests.form.get('westLightInt1', None)
        numCarsNorth = requests.form.get('northLightInt1', None)
        numCarsSouth = requests.form.get('southLightInt1', None)
        print(str(numCarsEast) + ' east')
        print(str(numCarsWest) + ' west')
        print(str(numCarsNorth) + ' north')
        print(str(numCarsSouth) + ' south')
        return 'done'
    return open('./carForm.html').read()
