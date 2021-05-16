from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def dojo_survey(cls):
        mysql = connectToMySQL('dojo_survey_schema')
        dojos = mysql.query_db('SELECT * FROM dojos;')

        results = []
        for dojo in dojos:
            results.append(cls(dojo))

        return results

    @staticmethod
    def validate_survey(dojo):
        is_valid = True
        if len(dojo['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        # if len(dojo['location']) != dojo['location']:
        #     flash("A location must be choosen.")
        #     is_valid = False
        # if len(dojo['languge']) != dojo['language']:
        #     flash("A language must be choosen.")
        #     is_valid = False
        if len(dojo['comments']) < 1:
            flash("A comment must be made.")
            is_valid = False
        return is_valid