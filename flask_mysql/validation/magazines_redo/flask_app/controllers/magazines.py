from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

from flask_app.models.magazine import Magazine
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('Log in to view dashboard')
        return redirect('/')

    magazines = Magazine.magazine_dashboard()

    user = User.get_user_by_id({'id' : session['user_id']})
    print(user)

    return render_template("dashboard.html", dashboard = magazines, user = user[0])

@app.route('/magazine/new')
def new_magazine():
    if 'email' not in session:
        flash('Log in to view dashboard')
        return redirect('/')
    return render_template("add_magazine.html")

@app.route('/add/magazine', methods=['POST'])
def add_magaizne():

    valid = Magazine.magazine_validator(request.form)

    if valid:
        data = {
            'title': request.form['title'],
            'description' : request.form['description'],
            'user_id': session['user_id']
        }

        Magazine.add_magazine(data)
        return redirect('/dashboard')

    return redirect('/magazine/new')

@app.route('/magazine/<int:id>')
def show_magazine(id):
    users = User.get_user_by_id({'id' : session['user_id']})
    magazines = Magazine.show_magazines({'id':id})
    magazine_user = User.get_user_by_id({'id': magazines[0]['users_id']})
    return render_template('show_magazine.html', users = users, magazines = magazines[0], magazine_user = magazine_user[0])



@app.route('/delete/<int:id>')
def delete_magazine(id):
    data = {
        'id':id
    }
    Magazine.delete_magazine(data)
    accounts = session['user_id']
    return redirect(f'/users/{accounts}')

@app.route('/users')
def user_account():
    user = User.get_user_by_id({'id' : session['user_id']})
    user_magazines = Magazine.get_by_users_id({'users_id' : session['user_id']})
    return render_template('user_account.html', user = user[0], user_magazines = user_magazines)

@app.route('/update', methods=["POST"])
def update_account():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id':session['user_id']
    }
    update = Magazine.update_user_account(data)
    accounts = session['user_id']
    return redirect(f'/users/{accounts}')