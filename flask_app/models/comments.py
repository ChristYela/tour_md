from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import date, datetime


class Comments:
    def __init__(self, data):
        self.id = data['id']
        self.place_id = data['place_id']
        self.user_id = data['user_id']
        self.comments = data['comments']

    @classmethod
    def save_comments(cls, data):
        query = "INSERT INTO comments ( place_id, user_id, comments) VALUES (%(place_id)s, %(user_id)s, %(comments)s)"
        result = connectToMySQL('tour').query_db(query, data)
        return result

    @classmethod
    def get_all(cls, data):
        query = "select * from comments where place_id = %(id)s"
        results = connectToMySQL('tour').query_db(query, data)
        coments = []
        for comentario in results:
            coments.append(cls(comentario))
        return coments
