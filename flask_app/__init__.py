import os

from flask import Flask

from config import PATH_TO_DB

if os.name == "posix":
    os.path.join(".")

from data import db_session
from routes import blueprint


db =  "." + PATH_TO_DB if os.name == "posix" else "flask_app" + PATH_TO_DB 

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"



def main():
    db_session.global_init(db)
    # app.register_blueprint
    app.run()


if __name__ == "__main__":
    main()
