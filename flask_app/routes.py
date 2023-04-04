import flask
import os

if os.name == "posix":
    from .data import db_session
elif os.name == "nt":
    from data import db_session



blueprint = flask.Blueprint(
    'routes',
    __name__,
    template_folder='templates'
)
