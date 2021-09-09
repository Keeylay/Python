from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
import re


bcrypt = Bcrypt (app)   

class Magazine():

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None


    @classmethod
    def magazine_dashboard(cls):
        mysql = connectToMySQL('belt_exam_schema')
        query = ("SELECT magazines.id AS id, magazines.title, magazines.description, magazines.created_at, magazines.updated_at, users_id AS users_id, users.first_name, users.last_name, users.email, users.password FROM magazines Join users on magazines.users_id = users.id;")
        results = mysql.query_db(query)

        magazines_list = []
        for item in results:
            magazine = cls(item)
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
            magazine.user = user
            magazines_list.append(magazine)
        
        return magazines_list

    @classmethod
    def add_magazine(cls, data):
        mysql = connectToMySQL('belt_exam_schema')
        query = "INSERT INTO magazines (title, description, users_id) VALUE ( %(title)s, %(description)s, %(user_id)s );"

        new_magazine = mysql.query_db(query, data)

        return new_magazine

    @classmethod
    def get_by_users_id(cls, data):
        mysql = connectToMySQL('belt_exam_schema')
        query = "SELECT * FROM magazines WHERE users_id =  %(users_id)s;"
        results = mysql.query_db(query, data)

        magazines_list = []
        for item in results:
            magazine = cls(item)
            magazines_list.append(magazine)

        return magazines_list

    @classmethod
    def get_magazine_by_id(cls,data):
        mysql = connectToMySQL('belt_exam_schema')
        query = "SELECT * FROM magazines WHERE id =  %(id)s;"
        results = mysql.query_db(query, data)

        magazines_list = []
        for item in results:
            magazine = cls(item)
            magazines_list.append(magazine)

        return magazines_list

    @classmethod
    def update_user_account(cls, data):
        mysql = connectToMySQL('belt_exam_schema')
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        results = mysql.query_db(query, data)

        return results

    @classmethod
    def show_magazines(cls, data):
        mysql = connectToMySQL('belt_exam_schema')
        query = "SELECT * FROM magazines WHERE id =  %(id)s;"
        show_magazines = mysql.query_db(query, data)

        return show_magazines

    @classmethod
    def delete_magazine(cls, data):
        mysql = connectToMySQL('belt_exam_schema')
        query = "DELETE FROM magazines WHERE id =  %(id)s;"
        return mysql.query_db(query, data)

    @staticmethod
    def magazine_validator(data):
        is_valid = True
        if len(data['title']) < 2:
            is_valid = False
            flash("Title must be longer than 2 characters.")

        if len(data['description']) < 10 or len(data['description']) > 500:
            is_valid = False
            flash("Description must be longer than 10 characters and shorter than 500 characters.")

        return is_valid