from flask import Flask
from flask import render_template , request 
from flask import current_app as app

@app.route("/")
def login_signup():
    return render_template("login_signup.html")

@app.route('/hello')
def hello():
    return 'hello'