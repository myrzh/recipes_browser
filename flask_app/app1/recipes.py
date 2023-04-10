from flask import jsonify, abort
from flask_restful import Resource

from app import main_app
from data import db_session
from data.recipes import Recipes
from flask_app.data import recipes


def abort_if_recipe_not_found(recipe_id):
    session = db_session.create_session()
    recipes = session.query(Recipes).get(recipe_id)
    if not recipes:
        abort(404, message=f"Recipe {recipe_id} not found")


class RecipeResource(Resource):
    def get(self, recipe_id):
        session = db_session.create_session()
        recipe = session.query(Recipes).get(recipe_id)
        if not recipe:
            abort(404, message=f"Recipe {recipe_id} not found")

        return jsonify({"recipe": recipe.to_dict(
            only=(
                "title",
                "grade",
                "text_content",
                # "photos_paths",
                "list_of_products",
                "is_private",
                "created_date",
                "liked_user_ids",
                "user_id"
                ))})

    def delete(self, recipe_id):
        session = db_session.create_session()
        recipe = session.query(Recipes).get(recipe_id)
        if not recipe:
            jsonify({"success": "OK"})
        
        session.delete(recipe)
        session.commit()
        return jsonify({"success": "OK"})

class RecipesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(Recipes).all()
        return jsonify({'news': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})
