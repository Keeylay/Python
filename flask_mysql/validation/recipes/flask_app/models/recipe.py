from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt = Bcrypt (app)   

class Recipe():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.preptime = data['preptime']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def recipe_dashboard(cls):
        mysql = connectToMySQL('users_recipes')
        recipes = mysql.query_db('SELECT * FROM recipes')

        results = []
        for recipe in recipes:
            results.append(cls(recipe))

        return results

    @classmethod
    def add_recipe(clr, data):
        mysql = connectToMySQL('users_recipes')
        query = "INSERT INTO recipes (name, description, instruction, preptime, user_id) VALUES ( %(name)s, %(description)s, %(instruction)s, %(preptime)s,  %(user_id)s);"

        new_recipe = mysql.query_db(query, data)

        return new_recipe

    @classmethod
    def show_edit(cls, data):
        mysql = connectToMySQL('users_recipes')
        query = "SELECT * FROM recipes WHERE id = %(id)s;"

        results = mysql.query_db(query, data)
        recipe = cls(results[0])

        return recipe

    @classmethod
    def edit_recipe(cls, data):
        mysql = connectToMySQL('users_recipes')
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, preptime = %(preptime)s WHERE id = %(id)s;"

        edit_recipe = mysql.query_db(query, data)

        return edit_recipe

    @classmethod
    def delete_recipe(cls, data):
        mysql = connectToMySQL('users_recipes')
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        return mysql.query_db(query, data)

    @staticmethod
    def recipe_validation(data):
        is_valid = True
        
        if len(data['name']) < 3:
            is_valid = False
            flash('Name must be longer than 3 characters')

        if len(data['description']) < 3 or len(data['description']) > 100:
            is_valid = False
            flash('Description must be longer than 3 characters')

        if len(data['instruction']) < 3 or len(data['instruction']) > 1000:
            is_valid = False
            flash('Instruction must be longer than 3 characters')

        # if data['preptime'] != 'yes' or data['preptime'] != 'no':
        #     is_valid = False
        #     flash('Please select Yes or No')

        return is_valid