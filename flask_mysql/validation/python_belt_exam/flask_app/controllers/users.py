from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def int():
    return render_template("index.html")

@app.route('/user/register', methods=['POST'])
def register_user():

    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'confirm_password':request.form['confirm_password']
    }
    
    valid = User.validate_registeration(data)

    if valid:
        User.create_user(data)
        flash("Account created, you can now log in!")

    return redirect('/dashboard')


@app.route('/login/user', methods = ["POST"])
def user_login():
    print(request.form)

    # results = User.email_valid(request.form)
    # if results == False:
    #     redirect('/')

    data = {
        'email':request.form['email']
    }

    user = User.get_user_by_email(data)
    if len(user) != 1:
        flash('email is invalid')
        return redirect('/')

    user = user[0]

    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user['id']
    session['email'] = user['email']

    return redirect('/dashboard')

@app.route('/logout/user')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/render/temp')
def render_user_stuff():

    if 'email' not in session:
        flash('Log in to view page')
        return redirect('/')

    return redirect('/dashboard')