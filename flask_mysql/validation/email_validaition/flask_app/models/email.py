from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email():

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def process_email(cls, data):
        mysql = connectToMySQL('email_validation_schema')
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        email = mysql.query_db(query, data)

        return email

    @staticmethod
    def validate_email(data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if len(data['email']) < 3:
            is_valid = False
            flash("Email needs to be longer than 3 characters.")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!")

        return is_valid
