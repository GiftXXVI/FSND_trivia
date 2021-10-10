from flask import Blueprint
from models import setup_db, Question, Category, get_db
from flask import Flask, request, abort, jsonify
import utilities
from utilities import paginate_questions, prepare_questions

categories_blueprint = Blueprint('categories_blueprint', __name__)

'''
@TODO:
Create an endpoint to handle GET requests
for all available categories.
'''

@categories_blueprint.route('/categories', methods=['GET'])
def get_categories():
    # try:
    categories = Category.query.order_by(Category.id).all()
    lcategories = len(categories)
    if lcategories == 0:
        abort(404)
    else:
        fcats = {cat.id: cat.type for cat in categories}
        return jsonify({"success": True, "categories": fcats})
    # except:
    #    abort(500)

    '''
  @TODO:
  Create a GET endpoint to get questions based on category.

  TEST: In the "List" tab / main screen, clicking on one of the
  categories in the left column will cause only questions of that
  category to be shown.
  '''


@categories_blueprint.route('/categories/<int:category_id>/questions', methods=['GET'])
def get_cat_questions(category_id):
    questions = Question.query.filter(Question.category == category_id).order_by(
        Question.category, Question.id).all()
    categories = Category.query.order_by(Category.id).all()
    fcats = {cat.id: cat.type for cat in categories}
    if len(questions) == 0:
        return abort(404)
    else:
        prepared_questions = prepare_questions(
            request, questions, fcats)
        return prepared_questions
