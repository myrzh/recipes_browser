from flask import Flask
import os

if os.name == "posix": os.path.join(".")
        

from data import db_session
from routes import blueprint

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("flask_app/db/db.sqlite")
    app.register_blueprint
    app.run()
