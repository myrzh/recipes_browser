from flask import Flask
# from flask_restful import Api
from flask

from data import db_session
from routes import blueprint


class App(Flask):
    def __init__(self, *args, **kwargs):

        super(App, self).__init__(*args, **kwargs)
        db_session.global_init("flask_app/db/db.sqlite")
        self.register_blueprint(blueprint)
        login_manager = LoginManager()
        login_manager.init_app(app)


main_app = App(__name__)
