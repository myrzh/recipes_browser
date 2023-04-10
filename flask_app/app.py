from flask import Flask

from data import db_session

from routes import blueprint

import os


class RecipesBrowser(Flask):
    def __init__(self, *args, **kwargs):
        super(RecipesBrowser, self).__init__(*args, **kwargs)
        db_session.global_init("flask_app/db/db.sqlite")
        self.register_blueprint(blueprint)
        SECRET_KEY = os.urandom(32)
        self.config["SECRET_KEY"] = SECRET_KEY


app = RecipesBrowser(__name__)
