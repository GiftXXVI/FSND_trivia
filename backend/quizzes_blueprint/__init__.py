from flask import Blueprint
from models import setup_db, Question, Category, get_db
from flask import Flask, request, abort, jsonify
from utilities import paginate_questions, prepare_questions
from sqlalchemy import not_
from random import choice

quizzes_blueprint = Blueprint('quizzes_blueprint', __name__)

'''
@TODO:
Create a POST endpoint to get questions to play the quiz.
This endpoint should take category and previous question parameters
and return a random questions within the given category,
if provided, and that is not one of the previous questions.

TEST: In the "Play" tab, after a user selects "All" or a category,
one question at a time is displayed, the user is allowed to answer
and shown whether they were correct or not.
'''


@quizzes_blueprint.route('/quizzes', methods=['POST'])
def get_quiz():
    body = request.get_json()
    if body is None:
        abort(400)
    else:
        previous_questions = body.get('previous_questions', [])
        quiz_category = body.get('quiz_category', None)        
        if quiz_category is None:
            abort(422)
        else:
            category_id = int(quiz_category['id'])
            if quiz_category['id'] == 0:
                questions = Question.query.filter(
                    not_(Question.id.in_(previous_questions))).all()
            else:
                questions = Question.query.filter(
                    not_(Question.id.in_(previous_questions)), Question.category == category_id).all()
            if len(questions) == 0:
                abort(404)
            else:
                available_questions = [question.format()
                                       for question in questions]
                next_question = choice(available_questions)
                return jsonify({
                    'success': True,
                    'question': next_question,
                    'quiz_category_id': quiz_category['id']
                })
