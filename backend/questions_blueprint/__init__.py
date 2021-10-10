from flask import Blueprint
from models import setup_db, Question, Category, get_db
from flask import Flask, request, abort, jsonify
import utilities
from utilities import paginate_questions, prepare_questions

questions_blueprint = Blueprint('questions_blueprint', __name__)


@questions_blueprint.route('/questions/test', methods=['GET'])
def test():
    return "Questions: Up and Up"

'''
@TODO:
Create an endpoint to handle GET requests for questions,
including pagination (every 10 questions).
This endpoint should return a list of questions,
number of total questions, current category, categories.

TEST: At this point, when you start the application
you should see questions and categories generated,
ten questions per page and pagination at the bottom of the screen for three pages.
Clicking on the page numbers should update the questions.
'''
@questions_blueprint.route('/questions', methods=['GET'])
def get_questions():
    try:
        questions = Question.query.order_by(
            Question.category, Question.id).all()

        categories = Category.query.order_by(Category.id).all()
        fcats = {cat.id: cat.type for cat in categories}
        if len(questions) == 0:
            return abort(404)
        else:
            prepared_questions = prepare_questions(
                request, questions, fcats)
            return prepared_questions
    except:
        abort(500)
'''
@TODO:
Create an endpoint to DELETE question using a question ID.

TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page.
'''
@questions_blueprint.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    question = Question.query.filter(
        Question.id == question_id).one_or_none()
    if question is None:
        abort(404)
    else:
        try:
            question.delete()
            question.dispose()
            return jsonify({
                'success': True,
                'deleted': question_id
            })
        except:
            question.rollback()
            question.dispose()
            abort(422)
'''
@TODO:
Create an endpoint to POST a new question,
which will require the question and answer text,
category, and difficulty score.

TEST: When you submit a question on the "Add" tab,
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.
'''
@questions_blueprint.route('/questions', methods=['POST'])
def create_question():
    body = request.get_json()
    if body is None:
        abort(400)
    else:
        question = body.get('question', None)
        answer = body.get('answer', None)
        difficulty = body.get('difficulty', None)
        category = body.get('category', None)
        if question is None or answer is None or difficulty is None or category is None:
            abort(400)
        else:
            try:
                question = Question(question=question, answer=answer,
                                    difficulty=difficulty, category=category)
                question.insert()
                question.refresh()
                question.dispose()
                return jsonify({
                    'success': True,
                    'created': question.id
                })
            except:
                question.rollback()
                question.dispose()
                abort(422)
'''
@TODO:
Create a POST endpoint to get questions based on a search term.
It should return any questions for whom the search term
is a substring of the question.

TEST: Search by any phrase. The questions list will update to include
only question that include that string within their question.
Try using the word "title" to start.
'''
@questions_blueprint.route('/questions/search', methods=['POST'])
def search_questions():
    body = request.get_json()
    if body is None:
        abort(400)
    else:
        search_term = body.get('searchTerm', None)
        fsearch = f'%{search_term}%'
        questions = Question.query.filter(Question.question.ilike(
            fsearch)).order_by(Question.category, Question.id).all()
        categories = Category.query.order_by(Category.id).all()
        fcats = {cat.id: cat.type for cat in categories}
        prepared_questions = prepare_questions(
            request, questions, fcats)
        return prepared_questions
