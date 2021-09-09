from types import MethodDescriptorType
from flask_app.config.sqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.car import Car


@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    
    cars = Car.get_all()
    return render_template('dashboard.html', cars = cars)


@app.route('/add_car')
def add_car():
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')

    return render_template("add_car.html")


@app.route('/create_car', methods = ['post'])
def create_car():
    if not Car.validate(request.form):
        return redirect('/add_car')
    data = {
        "year" : request.form['year'],
        "make" : request.form['make'],
        "model" : request.form['model'],
        "price" : request.form['price'],
        "description" : request.form['description'],
        "seller_id" : session['user_id']
    }

    new_car = Car.create_car(data)
    return redirect('/dashboard')


@app.route('/car/<int:id>')
def view_car(id):
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    data = {
        "id" :id
    }

    car = Car.get_car(data)

    return render_template('view_car.html', car = car)

@app.route('/edit/<int:id>')
def edit_car(id):
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')

    data = {
        "id" : id
    }

    car = Car.get_car(data)
    return render_template('edit_car.html', car = car)

@app.route('/update_car/<int:id>', methods= ['post'])
def update_car(id):
    if not Car.validate(request.form):
        return redirect('/add_car')
    data = {
        "id" : id,
        "year" : request.form['year'],
        "make" : request.form['make'],
        "model" : request.form['model'],
        "price" : request.form['price'],
        "description" : request.form['description'],
        "seller_id" : session['user_id']
    }

    new_car = Car.update_car(data)
    return redirect('/dashboard')

@app.route('/purchase/<int:id>', methods=['post'])
def purchase(id):
    data = {
        "id" : id,
        "purchaser_id" : session['user_id']
    }
    Car.purchase(data)
    return redirect('/dashboard')

@app.route('/user/<int:id>')
def show_purchases(id):
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    
    data = {
        "id" : id
    }
    cars = Car.show_purchases(data)
    return render_template('purchases.html', cars = cars)

@app.route('/delete/<int:id>')
def delete_car(id):
    data = {
        "id" : id,
        "user_id" : session["user_id"] 
    }
    Car.delete_car(data)
    return redirect ('/dashboard')