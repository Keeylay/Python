from flask.globals import request
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt = Bcrypt (app)   

class User():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['late_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(clr, data):

        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        print(hashed_pw)

        data['hashed_pw'] = hashed_pw

        mysql = connectToMySQL('user_login_registration_schema')
        query = "INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s, %(last_name)s, %(email)s, %(hashed_pw)s);"

        new_user_id = mysql.query_db(query, data)

        return new_user_id

    @classmethod
    def get_user_by_email(cls, data):
        
        mysql = connectToMySQL('user_login_registration_schema')
        query = "SELECT * FROM users WHERE email = %(email)s;"

        return mysql.query_db(query, data)

    @staticmethod
    def validate_registeration(data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

        if len(data['first_name']) < 3 or len(data['first_name']) > 30:
            is_valid = False
            flash("First name should be between 3 and 30 characters.")

        if len(data['last_name']) < 3 or len(data['last_name']) > 30:
            is_valid = False
            flash("Last name should be between 3 and 30 characters.")

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False

        mysql = connectToMySQL('user_login_registration_schema')
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = mysql.query_db(query, data)

        if len(results) != 0:
            is_valid = False
            flash('Email is already in use!')

        if len(data['password']) < 6:
            is_valid = False
            flash("Password should be at least 6 characters.")

        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Password and Confirm Password does not match.")

        return is_valid

    @staticmethod
    def email_valid(data):
        is_valid = True

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!")

        # mysql = connectToMySQL('user_login_registration_schema')
        # query = "SELECT * FROM users WHERE email = %(email)s;"
        # results = mysql.query_db(query, data)

        return is_valid