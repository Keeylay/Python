from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.dojo import Dojo

@app.route('/')
def data():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comments_from_form = request.form['comments']
    return render_template("results.html", name = name_from_form, location = location_from_form, language = language_from_form, comments = comments_from_form)