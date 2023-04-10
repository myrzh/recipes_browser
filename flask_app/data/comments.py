import sqlalchemy
from sqlalchemy import orm
from datetime import datetime

from .db_session import SqlAlchemyBase


class Comments(SqlAlchemyBase):
    __tablename__ = "comments"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    recipe_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("recipes.id")
    )

    text = sqlalchemy.Column(sqlalchemy.VARCHAR(), nullable=True)
