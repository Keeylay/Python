from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.dojo import Dojo

@app.route('/')
def data():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    if not Dojo.validate_survey(request.form):
        return redirect('/')
    Dojo.save(request.form)
    
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comments' : request.form['comments']
    }

    
    return render_template("results.html", data = data)
