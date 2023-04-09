import flask
import os

from data import db_session


blueprint = flask.Blueprint("routes", __name__, template_folder="templates")
