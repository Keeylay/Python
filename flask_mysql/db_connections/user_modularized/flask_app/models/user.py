from flask_app.config.mysqlconnection import connectToMySQL

class User():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        mysql = connectToMySQL('users_schema')
        users = mysql.query_db('SELECT * FROM users;')

        results = []
        for user in users:
            results.append(cls(user))

        return results