from app import app
from db import db
from flask import Flask, render_template, request
import requests, random, string, json

db.init_app(app)

# before the first request runs, it's going to create the database:
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def student():
   return render_template('home.html')


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

headers = {"Content-Type": "application/json"}

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		print(result['Price'])
		print(result['Id'])


        # payload = {
        # "price": result['Price'],
        # "store_id": result['Id']
        #       }
        # r = requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), headers=headers, data=json.dumps(payload))


		return render_template("result.html",result = result)
