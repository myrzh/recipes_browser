import sqlalchemy
from sqlalchemy import orm
from datetime import datetime

from .db_session import SqlAlchemyBase


class Recipes(SqlAlchemyBase):
    __tablename__ = "recipes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    grade = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    text_content = sqlalchemy.Column(sqlalchemy.VARCHAR(), nullable=True)

    photos_paths = sqlalchemy.Column(sqlalchemy.VARCHAR(), nullable=True)
    
    list_of_products = sqlalchemy.Column(sqlalchemy.VARCHAR(), nullable=True)
    
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)

    liked_users_ids = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True
    )

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    comments = orm.relationship("Comments", backref="recipes")
