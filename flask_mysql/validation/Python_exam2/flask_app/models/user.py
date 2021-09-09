from flask import flash
from flask_app.config.sqlconnection import MySQLConnection

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.pass_has = data['pass_hash']
        self.email_address = data['email_address']
        self.spam_ok = data['spam_ok']

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters long.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters long.")
            is_valid = False
        if (len(data['password']) < 8 or len(data['password']) > 20):
            flash('Password must be between 8 and 20 characters')
            is_valid = False
        if data['password'] != data['password_verify']:
            flash('Password and Password Verification do not match.')
            is_valid = False
        
        return is_valid

    @staticmethod
    def validate_edit(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters long.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters long.")
            is_valid = False
        
        
        return is_valid
    
    @staticmethod
    def login_validate(data):
        is_valid = True
        mysql = MySQLConnection('exam_schema')
        query = ("select * from users where email_address = %(email_address)s")
        user_check = mysql.query_db(query, data)
        if len(user_check) != 1:
            is_valid=False
            flash('Username or Password is invalid')
        return is_valid

    @classmethod
    def is_unique(cls, data):
        is_valid = True
        mysql = MySQLConnection('exam_schema')
        query = ("select * from users where email_address = (%(email)s)")
        test = mysql.query_db(query, data)
        if len(test) > 0:
            is_valid = False
        return is_valid

    @classmethod
    def add_user(cls, data):
        mysql = MySQLConnection('exam_schema')
        query = ("insert into users (email_address, pass_hash, first_name, last_name, spam_ok) values (%(email)s, %(password)s, %(first_name)s, %(last_name)s, %(spam_ok)s)")

        new_email = mysql.query_db(query, data)
        return new_email

    @classmethod
    def get_user(cls, data):
        mysql = MySQLConnection('exam_schema')
        query = ("select * from users where email_address = %(email_address)s")
        user = mysql.query_db(query, data)
        return user
    
    @classmethod
    def update_user(cls, data):
        mysql = MySQLConnection('exam_schema')
        query = ("update users set first_name = %(first_name)s, last_name = %(last_name)s, email_address = %(email)s where id = %(user_id)s;")

        updated = mysql.query_db(query, data)
        return updated
