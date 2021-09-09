from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app


class Comment():

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.message_id = data['message_id']
        self.user_id = data['user_id']
        self.user_nickname = data['nickname']

    @classmethod
    def create_comment(cls, data):
        connection = connectToMySQL('wall_demo')
        query = "INSERT INTO comments (content, message_id, user_id) VALUES (%(content)s, %(message_id)s, %(user_id)s);"
        new_comment_id = connection.query_db(query, data)

        return new_comment_id

    @classmethod
    def comments_for_message(cls, data):
        connection = connectToMySQL('wall_demo')
        query = "SELECT comments.id as id, content, message_id, user_id, comments.created_at as created_at, comments.updated_at as updated_at, nickname FROM comments JOIN users ON users.id = comments.user_id WHERE message_id = %(id)s;"
        results = connection.query_db(query, data)

        comments = []

        for item in results:

            print(item)
            comments.append(cls(item))

        return comments

    @staticmethod
    def validate_comment(data):

        is_valid = True

        if len(data['content']) < 5:
            is_valid = False
            flash('Comment should be at least five characters!')

        if len(data['content']) > 1000:
            is_valid = False
            flash('nobody will read that, write a shorter comment')

        return is_valid