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
    print(magazines)

    return render_template("dashboard.html", dashboard = magazines)

@app.route('/magazine/new')
def new_magazine():
    if 'email' not in session:
        flash('Log in to view dashboard')
        return redirect('/')
    return render_template("add_magazine.html")

@app.route("/add/magazine", methods=['POST'])
def add_magazine():

    valid = Magazine.magazine_validation(request.form)

    if valid:
        data = {
            'title' : request.form['title'],
            'description' : request.form['description'],
            'user_id': session['user_id']
        }

        Magazine.add_magazine(data)
        return redirect("/dashboard")

    return redirect('/magazine/new')




    

@app.route('/magazine/<int:id>/<first_name>')
def show_magazine(id, first_name):
    data = {
        'magazine' : Magazine.show_edit(),
        'first_name': first_name
    }
    return render_template('show_magazine.html', magazine = Magazine.show_edit({'id': id}))

@app.route('/user/<int:user_id>')
def user_account():
    return render_template('user_account.html')
