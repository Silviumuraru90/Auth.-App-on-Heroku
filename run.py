from app import app
from db import db
from flask import Flask, render_template

db.init_app(app)

# before the first request runs, it's going to create the database:
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template("home.html")
