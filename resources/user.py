import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This fied is required")

    parser.add_argument('password',
            type=str,
            required=True,
            help="this fied is required")

    def post(self):
        """Method to signup user"""
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                "message":"An account with that username already exists"
                },400
        user = UserModel(**data)
        user.save_to_db()

        return {"message":"User created successfully."}, 201
