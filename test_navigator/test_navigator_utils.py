import requests
from flask import make_response, jsonify
from flask_api.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from flask_restful import fields, marshal

from test_navigator.test_navigator_model import UserData

user_fields = {'id': fields.Integer,
               'name': fields.String}

user_list_fields = {'count': fields.Integer,
                    'users': fields.List(fields.Nested(user_fields))}


def get_hello_word():
    return 'hello'


def get_world_word():
    return 'world'


def get_phrase():
    return get_hello_word() + ' ' + get_world_word()


def get_users():
    users = UserData.get_all()
    if not users:
        return make_response(jsonify({'error': 'The user database is empty'}), HTTP_404_NOT_FOUND)
    else:
        try:
            content = marshal({'count': len(users), 'users': [marshal(u, user_fields) for u in users]},
                              user_list_fields)
        except:
            return make_response({'error': 'Corrupted database data'}, HTTP_500_INTERNAL_SERVER_ERROR)

        return make_response(content, HTTP_200_OK)


def add_user(user_name):
    UserData.create(user_name)
