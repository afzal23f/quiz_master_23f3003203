from flask import current_app as app

@app.route("/login")
def login():
    return 'login'

@app.route("/signup")
def signup():
    return 'signup'