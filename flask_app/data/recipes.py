import sqlalchemy
from sqlalchemy import orm
from datetime import datetime

from .db_session import SqlAlchemyBase


class Recipes(SqlAlchemyBase):
    __tablename__ = "recipes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    text_content = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)

    photos_paths = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))

    list_of_products = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)

    user = orm.relationship("User")
