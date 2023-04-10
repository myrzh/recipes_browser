from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from data import db_session


class App(Flask):
    def __init__(self, *args, **kwargs):

        super(App, self).__init__(*args, **kwargs)
        db_session.global_init("flask_app/db/db.sqlite")
        self.jwt = JWTManager(self)
        self.config.from_pyfile("config.py")
        self.api = Api(self)
        self.jwt = JWTManager(self)


main_app = App(__name__)


@main_app.jwt.expired_token_loader
def my_expired_token_callback():
    err_json = {"message": "expired_token"}
    return jsonify(err_json), 401


@main_app.jwt.invalid_token_loader
@main_app.jwt.unauthorized_loader
def my_inv_unauth_token_callback(why):
    err_json = {"message": why}
    return jsonify(err_json), 401
