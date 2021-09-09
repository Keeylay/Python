from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
import re


bcrypt = Bcrypt (app)   

class Car():

    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.price = data['price']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def car_dashboard(cls):
        mysql = connectToMySQL('car_deals_schema_exam')
        query = ("SELECT cars.id AS id, cars.make, cars. model, cars.price, cars.year, cars.description, cars.created_at, cars.updated_at, users_id AS users_id, users.first_name, users.last_name, users.email, users.password FROM cars Join users on cars.users_id = users.id;")
        results = mysql.query_db(query)

        cars_list = []
        for item in results:
            car = cls(item)
            user_data = {
                'id':item['users_id'],
                'first_name' : item['first_name'],
                'last_name' : item['last_name'],
                'email' : item['email'],
                'password':item['password'],
                'created_at' : item['created_at'],
                'updated_at' : item['updated_at']
            }

            user = User(user_data)
            car.user = user
            cars_list.append(car)
        
        return cars_list

    @classmethod
    def add_car(cls, data):
        mysql = connectToMySQL('car_deals_schema_exam')
        query = "INSERT INTO cars (make, model, price, year, description, users_id) VALUE ( %(make)s, %(model)s, %(price)s, %(year)s, %(description)s, %(user_id)s );"

        new_car = mysql.query_db(query, data)

        return new_car

    @classmethod
    def get_by_users_id(cls, data):
        mysql = connectToMySQL('car_deals_schema_exam')
        query = "SELECT * FROM cars WHERE id =  %(id)s;"
        results = mysql.query_db(query, data)
        car = cls(results[0])
        return car

    @classmethod
    def update_car(cls, data):
        mysql = connectToMySQL('car_deals_schema_exam')
        query = "UPDATE cars SET make = %(make)s, model = %(model)s, price = %(price)s, year = %(year)s, description = %(description)s WHERE id = %(id)s;"

        update_car = mysql.query_db(query, data)

        return update_car

    @classmethod
    def show_cars(cls, data):
        mysql = connectToMySQL('car_deals_schema_exam')
        query = "SELECT * FROM cars WHERE id =  %(id)s;"
        show_cars = mysql.query_db(query, data)

        return show_cars

    @classmethod
    def delete_car(cls, data):
        mysql = connectToMySQL('car_deals_schema_exam')
        query = "DELETE FROM cars WHERE id =  %(id)s;"
        return mysql.query_db(query, data)



    @staticmethod
    def car_validator(data):
        is_valid = True
        if len(data['make']) < 3:
            is_valid = False
            flash("Make must be longer than 3 characters.")

        if len(data['model']) < 3:
            is_valid = False
            flash("Model must be longer than 3 characters.")

        if len(data['price']) < 0:
            is_valid = False
            flash("Price must be greater than 0.")

        if len(data['year']) < 0:
            is_valid = False
            flash("Year must be greater than 0.")

        if len(data['description']) < 10 or len(data['description']) > 500:
            is_valid = False
            flash("Description must be longer than 10 characters and shorter than 500 characters.")

        return is_valid