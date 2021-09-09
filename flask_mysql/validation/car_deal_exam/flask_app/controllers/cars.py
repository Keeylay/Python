from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

from flask_app.models.car import Car
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('Log in to view dashboard')
        return redirect('/')

    cars = Car.car_dashboard()

    users = User.get_user_by_id({'id' : session['user_id']})

    return render_template("dashboard.html", dashboard = cars, users = users[0])

@app.route('/new')
def car_posting():
    if 'email' not in session:
        flash('Log in to view dashboard')
        return redirect('/')
    return render_template("add_car.html")

@app.route('/add/car', methods=['POST'])
def add_car():
    valid = Car.car_validator(request.form)

    if valid:
        data = {
            'make': request.form['make'],
            'model': request.form['model'],
            'price': request.form['price'],
            'year': request.form['year'],
            'description' : request.form['description'],
            'user_id': session['user_id']
        }

        Car.add_car(data)
        return redirect('/dashboard')

    return redirect('/new')

@app.route('/edit/<int:id>')
def edit_car(id):
    user_cars = Car.get_by_users_id({'id':id})
    return render_template('edit_car.html', car = user_cars)

@app.route('/car/update', methods=['POST'])
def update_car():
    valid = Car.car_validator(request.form)

    if valid:
        data = {
            'id':request.form['id'],
            'make': request.form['make'],
            'model': request.form['model'],
            'price': request.form['price'],
            'year': request.form['year'],
            'description' : request.form['description'],
            # 'id':session['user_id']
        }

        Car.update_car(data)
        return redirect('/dashboard')
    car = request.form['id']
    return redirect(f'/edit/{car}')

@app.route('/show/<int:id>')
def show_cars(id):
    # users = User.get_user_by_id({'id' : session['user_id']})
    cars = Car.show_cars({'id':id})
    car_user = User.get_user_by_id({'id': cars[0]['users_id']})
    return render_template('show_car.html', car = cars[0], car_user = car_user[0])

@app.route('/purchase/<int:id>')
def purchase(id):
    data = {
        'id':id
    }
    Car.delete_car(data)
    return redirect('/dashboard')
