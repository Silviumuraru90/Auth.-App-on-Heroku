from app import app
from db import db
from flask import Flask, render_template, request, url_for, redirect
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

#headers = {"Content-Type": "application/json"}

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        global result = request.form
        requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps({"price":result['Price'], "store_id":result['Id']}), headers={"Content-Type": "application/json"})
    return render_template("result.html",result = result)




# payload = {
# "price": result['Price'],
# "store_id": result['Id']
#}

# requests.post("https://ecnaoptriha.herokuapp.com/item/klisssssda".format(id_generator()), data=json.dumps({"price":15.99, "store_id":1}), headers={"Content-Type": "application/json"})

#requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps(payload), headers=headers)
