from flask import current_app as app, render_template, request, redirect, url_for, flash
from models.model import *

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/add_subject", methods= ["POST", "GET"])
def add_subject():
    if request.method == 'POST':
        id = request.form['subject_id']
        subject_name = request.form['subject_name']
        description = request.form['description']

        existing_subject = Subject.query.filter_by(id=id).first()

        if existing_subject:
            flash("subject Already Exits.." ,"Error")
            return redirect(url_for('add_subject'))
        else:
            new_subject = Subject(id=id, name = subject_name, description = description)
            db.session.add(new_subject)
            db.session.commit()
            flash("subject Added Succeffully.." ,"Success")
            return redirect(url_for('add_subject'))

    return render_template("admin/add_subject.html")