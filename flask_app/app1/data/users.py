import datetime
import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager


from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    nickname = sqlalchemy.Column(sqlalchemy.VARCHAR(20), nullable=True)

    admin = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    email = sqlalchemy.Column(sqlalchemy.VARCHAR(40), index=True, unique=True, nullable=True)

    hashed_password = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    
    recipes = orm.relationship("Recipes", back_populates='users')

    comments = orm.relationship("Comments", back_populates="users")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)