from app import app
from db import db
from flask import Flask, render_template, request

db.init_app(app)

# before the first request runs, it's going to create the database:
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def student():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		print(result['Item'])
		print(result['Price'])
		return render_template("result.html",result = result)
