from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.email import Email

@app.route('/')
def submit():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def verify_email():

    data = {
        'email': request.form['email']
    }

    valid = Email.validate_email(data)
    
    if valid:
        Email.process_email(data)

    return redirect('/')