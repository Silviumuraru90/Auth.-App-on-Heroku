import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
import re


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,.]')
    if(regex.search(string) is None):
        return True
    return False

def passuser(user, password):
    for i in range(len(user)):
        if i < (len(user) - 2):
            for n in range(len(password)):
                if n < (len(password) - 2):
                    if user[i] == password[n] and user[i+1] == password[n+1] and user[i+2] == password[n+2]:
                        return True
    return False

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required=True,
        help = "This field cannot be blank!"
    )
    parser.add_argument('password',
        type = str,
        required=True,
        help = "This field cannot be blank!"
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username'].lower()):
            return {"message": "A user with that username already exists"}, 400

        # user = UserModel(data['username'], data['password'])     OR
        user = UserModel(**data)

        if len(user.username) != len(user.username.strip()) and len(user.password) != len(user.password.strip()):
            return {"message": "Please do not include trailing spaces. They are permitted only within the string of chars in either username or password."}, 400

        if len(user.username) not in range (5,11):
            return {"message": "The username should have in between 5 and 10 chars!"}, 400

        if len(user.password) < 10:
            return {"message": "The password should have at least 10 chars!"}, 400

        if str.islower(user.password):
            return {"message": "The password should contain uppercase chars as well!"}, 400

        if str.isupper(user.password):
            return {"message": "The password should contain lowercase chars as well!"}, 400

        if hasNumbers(user.password) is False:
            return {"message": "The password should contain at least one number!"}, 400

        if run(user.password) is True:
            return {"message": """The password should contain either of the
                    following special symbols: [@_!#$%^&*()<>?/\|}{~:,.]"""}, 400

        if passuser(user.username, user.password) is True:
            return {"message": "Password contains parts of the username!"}, 400

        user.save_to_db()

        return {
            'message': "User created successfully."
        }, 201
