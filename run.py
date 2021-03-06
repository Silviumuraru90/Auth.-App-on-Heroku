# import win32api

import smtplib, ssl
import os

from app import app
from db import db
from flask import render_template, request  # ,Flask, url_for, redirect
import random, string  # json, requests

#from flask import jsonify

from security import authenticate, identity
from flask_jwt import JWT

from models.item import ItemModel
from models.user import UserModel

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address, default_limits=["35 per hour"])


db.init_app(app)

# before the first request runs, it's going to create the database:
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
@limiter.limit("3 per day")
def register():
    return render_template('register.html')


@app.route('/home', methods=["POST", "GET"])
def home():
    username = request.form["username"].lower()
    password = request.form["password"]
    user = UserModel.find_by_username(username)
    if user and user.password == password and len(user.username) in range (5,10):

#         address = request.environ['REMOTE_ADDR']
        
        # address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        
        # address = request.remote_addr
        
        # from mod_python import apache
        # req.get_remote_host(apache.REMOTE_NOLOOKUP)
        
#         port = 465
#         smtp_server = "smtp.gmail.com"
#         sender_email = "pythontesting222@gmail.com"
#         receiver_email = "silviumuraru90@gmail.com"
#         emailpass = UserModel.find_by_username("adminao")
#         password = emailpass.password

#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#             server.login(sender_email, password)
#             message = """\
#         Subject: Someone accessed your app

#         IP [{}]. User [{}] just logged into your app.""".format(address, user.username, password)
#             server.sendmail(sender_email, receiver_email, message)

        return render_template('home.html', user=username)     #, ip = address)

        # jwt = JWT(app, authenticate, identity)
        # return jwt

    # raise Exception('Sign In failed!')
    return render_template('login.html'), 400  # win32api.MessageBox(0, 'hello', 'title')


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# headers = {"Content-Type": "application/json"}

# def functie(x):
#     return requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps({"price":x['Price'], "store_id":x['Id']}), headers={"Content-Type": "application/json"})


a = dict()

@app.route('/result', methods=['POST', 'GET'])
@limiter.limit("10 per hour", exempt_when=lambda: request.method == 'POST')
def result():
    global a
    if request.method == 'POST':
        result = request.form

#       a = dict(zip(a.keys(),a.values())) - not a good use-case, as it cannot
#                                              be sliced and have its indices
#                                              used otherwise it would've done
#                                              the job.

        for elem in result:
            keys = list(result.keys())
            values = list(result.values())
        a = dict(zip(keys[:2], values[:2]))

        # functie(result)
        item = ItemModel(id_generator(), **a)
        item.save_to_db()
        # a = result

    # return redirect("http://ecnaoptriha.herokuapp.com/result", code=302)
    return render_template("result.html", result=a)


# a = ''

# @app.route('/result', methods = ['POST', 'GET'])
# def result():
#     global a
#     if request.method == 'POST':
#         result = request.form
#         a = result
#     # return redirect("http://ecnaoptriha.herokuapp.com/result", code=302)
#     return render_template("result.html",result = a)

# def something():
#     global a
#     if a:
#         functie(a)

# payload = {
# "price": result['Price'],
# "store_id": result['Id']
# }

# requests.post("https://ecnaoptriha.herokuapp.com/item/klisssssda".format(id_generator()), data=json.dumps({"price":15.99, "store_id":1}), headers={"Content-Type": "application/json"})
# '**data' is   data['price'], data['store_id']
# requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps(payload), headers=headers)
