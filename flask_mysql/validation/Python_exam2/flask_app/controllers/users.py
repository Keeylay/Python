from flask_app.config.sqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.car import Car

from flask_bcrypt import Bcrypt

import re
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    print(request.form)
    if not User.validate(request.form):
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        return redirect('/')
    pass_check = re.findall('\d.*[A-Z]|[A-Z].*\d', request.form['password'])
    if not pass_check:
        flash('Password must contain one uppercase letter or number')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "email" : request.form['email'],
        "password" : pw_hash,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
    }
    if 'spam' in request.form:
        data['spam_ok'] = 1
    else:
        print('nope')
        data['spam_ok'] = 0
    
    if not User.is_unique(data):
        flash("Email address already in use.")
        return redirect('/')
    
    new_user = User.add_user(data)
    print(new_user)
    flash("You have successfully registered")
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    session['user_id'] = new_user
    session['email'] = data['email']
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    data = {
        "email_address" : request.form['login_email'],
    }
    if not EMAIL_REGEX.match(request.form['login_email']):
        flash("Invalid Email Address")
        return redirect('/')

    if not User.login_validate(data):
        return redirect('/')
    user = User.get_user(data)
    user = user[0]
    print(user)
    if not bcrypt.check_password_hash(user['pass_hash'], request.form['login_password']):
        flash('Username or Password is invalid')
        return redirect('/')
    session['user_id'] = user['id']
    session['email'] = user['email_address']
    session['first_name'] = user['first_name']
    session['last_name'] = user['last_name']
    return redirect('dashboard')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect('/')

