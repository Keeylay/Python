from flask import flash
from flask_app.config.sqlconnection import MySQLConnection
from flask_app.models.user import User


class Car:
    def __init__(self, data):
        self.id = data['id']
        self.year = data['year']
        self.make = data['make']
        self.model = data['model']
        self.price = data['price']
        self.description = data['description']
        self.seller_id = data['seller_id']
        self.purchaser_id = data['purchaser_id']
        self.user = User(data)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['make']) < 1:
            flash('Make cannot be blank')
            is_valid = False
        if len(data['model']) < 1:
            flash('Model cannot be blank')
            is_valid = False
        if len(data['year']) < 1 or int(data['year']) < 1:
            flash('Year must be greater than 0')
            is_valid = False
        if len(data['price']) < 1 or int(data['price']) < 1:
            flash('Price must be greater than 0')
            is_valid = False
        if len(data['description']) < 10:
            flash('Desctription should be at least 10 characters')
            is_valid = False
        return is_valid

    @classmethod
    def create_car(cls, data):
        mysql = MySQLConnection('exam_schema')
        query = ("insert into cars (year, make, model, price, description, seller_id) values (%(year)s, %(make)s, %(model)s, %(price)s, %(description)s, %(seller_id)s )")
        new_car = mysql.query_db(query, data)
        return new_car

    @classmethod
    def get_all(cls):
        mysql = MySQLConnection('exam_schema')
        query = ("select * from cars join users on cars.seller_id = users.id")
        carQ = mysql.query_db(query)
        cars = []
        for car in carQ:
            new = Car(car)
            cars.append(new)
        return cars

    @classmethod
    def get_car(cls, data):
        mysql = MySQLConnection('exam_schema').query_db('select * from cars join users on cars.seller_id = users.id where cars.id = %(id)s;', data)
        mysql = mysql[0]
        car = Car(mysql)
        return car

    @classmethod
    def update_car(cls, data):
        mysql = MySQLConnection('exam_schema').query_db('update cars set year = %(year)s, price = %(price)s, model = %(model)s, make = %(make)s, description = %(description)s where cars.id = %(id)s;', data)

    @classmethod
    def purchase(cls, data):
        mysql = MySQLConnection('exam_schema').query_db("update cars set purchaser_id = %(purchaser_id)s, is_sold = '1' where cars.id = %(id)s;", data)

    @classmethod
    def show_purchases(cls, data):
        mysql = MySQLConnection('exam_schema')
        query = ("select * from cars join users on cars.purchaser_id = users.id where cars.purchaser_id = %(id)s ;")
        carQ = mysql.query_db(query, data)
        cars = []
        for car in carQ:
            new = Car(car)
            cars.append(new)
        return cars

    @classmethod
    def delete_car(cls, data):
        mysql = MySQLConnection('exam_schema').query_db('delete from cars where id = %(id)s and seller_id = %(user_id)s;', data)