import flask
import os

if os.name == "posix":
    os.path.join(".")

from data import db_session


blueprint = flask.Blueprint("routes", __name__, template_folder="templates")
