import os

from flask import Flask

if os.name == "posix":
    from .data import db_session
    from .routes import blueprint
elif os.name == "nt":
    from data import db_session
    from routes import blueprint


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("flask_app/db/db.sqlite")
    # app.register_blueprint
    app.run()


if __name__ == "__main__":
    main()
