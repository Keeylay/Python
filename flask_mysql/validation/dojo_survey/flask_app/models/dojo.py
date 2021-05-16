from flask_mysql.validation.dojo_survey.flask_app.controllers.dojos import results
from flask_app.config.mysqlconnection import connectToMySQL

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