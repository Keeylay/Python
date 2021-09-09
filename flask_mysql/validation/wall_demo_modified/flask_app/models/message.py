from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.comment import Comment

class Message():

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.comments = []

    @classmethod
    def create_message(cls, data):
        connection = connectToMySQL('wall_demo')
        query = "INSERT INTO messages (user_id, content) VALUES (%(user_id)s, %(content)s)"
        new_message_id = connection.query_db(query, data)

        return new_message_id

    @classmethod
    def get_one_message(cls, data):
        connection = connectToMySQL('wall_demo')
        query = "SELECT * FROM messages WHERE messages.id = %(id)s;"
        results = connection.query_db(query, data)

        if len(results) == 0:
            return None

        else:
            result = results[0]
            message = cls(result)
            message.user_id = result['user_id']
            message.user = User.get_user_by_id({'id': result['user_id']})
            message.comments = Comment.comments_for_message(data)

            return message

    @classmethod
    def get_all_messages(cls):
        connection = connectToMySQL('wall_demo')
        query = "SELECT messages.id AS id, messages.content, messages.created_at, messages.updated_at, users.id AS user_id, users.nickname, users.email, users.password, users.created_at AS user_created_at, users.updated_at AS user_updated_at FROM messages JOIN users on messages.user_id = users.id;"
        results = connection.query_db(query)

        messages = []

        for item in results:
            message = cls(item)
            user_data = {
                'id': item['user_id'],
                'nickname': item['nickname'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['user_created_at'],
                'updated_at': item['user_updated_at']
            }
            user = User(user_data)
            message.user = user
            messages.append(message)

        return messages

    @classmethod
    def delete_message(cls, data):
        connection = connectToMySQL('wall_demo')
        query = "DELETE FROM messages WHERE id = %(id)s;"
        connection.query_db(query, data)

    @classmethod
    def update_message(cls, data):
        connection = connectToMySQL('wall_demo')
        query = "UPDATE messages SET content = %(content)s WHERE id = %(id)s;"
        connection.query_db(query, data)

    @staticmethod
    def validate_message(data):

        is_valid = True

        if len(data['content']) < 5:
            is_valid = False
            flash('Message should be at least five characters!')

        if len(data['content']) > 1000:
            is_valid = False
            flash('nobody will read that, write a shorter message')

        return is_valid