from flask import Flask

from data import db_session

from routes import blueprint


class RecipesBrowser(Flask):

    def __init__(self, *args, **kwargs):

        super(RecipesBrowser, self).__init__(*args, **kwargs)
        db_session.global_init("flask_app/db/db.sqlite")
        self.register_blueprint(blueprint)


app = RecipesBrowser(__name__)
