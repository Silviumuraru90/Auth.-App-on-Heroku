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

def functie(x):
    return requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps({"price":x['Price'], "store_id":x['Id']}), headers={"Content-Type": "application/json"})

a = dict()    
    
@app.route('/result', methods = ['POST', 'GET'])
def result():
    global a
    if request.method == 'POST':
        result = request.form
        
        # a = dict(zip(a.keys(),a.values())) - not a good use-case, as it cannot be sliced and have its indices used
        
        for elem in result:
            keys = list(result.keys())
            values = list(result.values())
        a = dict(zip(keys[:2], values[:2]))
        
        functie(result)
        
        # a = result
        
    # return redirect("http://ecnaoptriha.herokuapp.com/result", code=302)
    return render_template("result.html",result = a)
    




# a = ''

# @app.route('/result', methods = ['POST', 'GET'])
# def result():
#     global a
#     if request.method == 'POST':
#         result = request.form
#         a = result
#     # return redirect("http://ecnaoptriha.herokuapp.com/result", code=302)
#     return render_template("result.html",result = a)

# def cacau():
#     global a
#     if a:
#         functie(a)

# payload = {
# "price": result['Price'],
# "store_id": result['Id']
# }

# requests.post("https://ecnaoptriha.herokuapp.com/item/klisssssda".format(id_generator()), data=json.dumps({"price":15.99, "store_id":1}), headers={"Content-Type": "application/json"})

#requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps(payload), headers=headers)
