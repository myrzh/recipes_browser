from flask import abort, jsonify
from flask_restful import Resource, reqparse


from data import db_session
from data.users import Users
from app import main_app


parser = reqparse.RequestParser()
parser.add_argument("nickname", required=True)
parser.add_argument("email", required=True)
parser.add_argument("password", required=True)


class RegisterResource(Resource):

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(Users).get(args["nickname"])
        if user is None:
            user = Users(
                    nickname=args["nickname"],
                    admin=False,
                    email=args["email"],
                    hashed_password=args["password"]
            )
            session.add(user)
            session.commit()

            return jsonify({'success': 'OK'})
        
        return abort(400, "duplicated username")

class LoginResource(Resource):

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(Users).get(args["nickname"])
        if user is None:
            return abort(400, "duplicated username")

        return jsonify({'success': 'OK'})

