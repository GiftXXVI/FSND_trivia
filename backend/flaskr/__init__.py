from operator import not_
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import not_
from flask_cors import CORS
import random
from math import ceil


from models import setup_db, Question, Category, get_db

QUESTIONS_PER_PAGE = 10


def paginate_questions(page, questions):
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    fquestions = [question.format() for question in questions]
    pquestions = fquestions[start:end]
    lquestions = len(fquestions)
    plquestions = len(pquestions)
    npages = ceil(lquestions/QUESTIONS_PER_PAGE)

    return pquestions, lquestions, plquestions, npages


def prepare_questions(request, questions, lcategory):
    page = request.args.get('page', 1, type=int)
    paginated_questions, length_questions, page_size, num_pages = paginate_questions(
        page, questions)

    if page_size == 0:
        curr_cat = ''
    else:
        ccategory = paginated_questions[len(
            paginated_questions) - 1]['category']
        curr_cat = lcategory[ccategory]
    return jsonify({
        'success': True,
        'page_num': page,
        'curr_page_size': page_size,
        'num_pages': num_pages,
        'totalQuestions': length_questions,
        'questions': paginated_questions,
        'currentCategory': curr_cat,
        'categories': lcategory
    })


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    db = get_db()
    migrate = Migrate(app, db)

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
    CORS(app)

    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, DELETE, POST')
        return response

    '''
  @TODO:
  Create an endpoint to handle GET requests
  for all available categories.
  '''
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.order_by(Category.id).all()
        lcategories = len(categories)
        if lcategories == 0:
            abort(404)
        else:
            fcats = {cat.id: cat.type for cat in categories}
            return jsonify({"categories": fcats})
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
    @app.route('/questions', methods=['GET'])
    def get_questions():
        questions = Question.query.order_by(
            Question.category, Question.id).all()

        categories = Question.query.order_by(
            Question.category, Question.id).with_entities(Question.category).all()

        lcategory = list(set([Category.query.filter_by(
            id=item.category).one_or_none() for item in categories]))
        fcats = {cat.id: cat.type for cat in lcategory}
        if len(questions) == 0:
            return abort(404)
        else:
            prepared_questions = prepare_questions(
                request, questions, fcats)
            return prepared_questions
    '''
  @TODO:
  Create an endpoint to DELETE question using a question ID.

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page.
  '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.filter_by(
            Question.id == question_id).one_or_none()
        if question is None:
            abort(404)
        else:
            try:
                question.delete()
                return jsonify({
                    'success': True
                })
            except:
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
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        if body is None:
            abort(400)
        else:
            question = body.get('question', None)
            answer = body.get('answer', None)
            difficulty = body.get('difficulty', None)
            category = body.get('category', None)
            try:
                question = Question(question=question, answer=answer,
                                    difficulty=difficulty, category=category)
                question.insert()
                return jsonify({
                    'success': True
                })
            except:
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
    @app.route('/questions/search', methods=['POST'])
    def search_posts():
        body = request.get_json()
        if body is None:
            abort(400)
        else:
            search_term = body.get('searchTerm', None)
            fsearch = f'%{search_term}%'
            try:
                questions = Question.query.filter(Question.question.ilike(
                    fsearch)).order_by(Question.category, Question.id).all()
                categories = Question.query.filter(Question.question.ilike(fsearch)).order_by(
                    Question.category, Question.id).with_entities(Question.category).distinct().all()
                lcategory = list(set([Category.query.filter_by(
                    id=item.category).one_or_none() for item in categories]))
                fcats = {cat.id: cat.type for cat in lcategory}
                if len(questions) == 0:
                    return abort(404)
                else:
                    prepared_questions = prepare_questions(
                        request, questions, fcats)
                    return prepared_questions
            except:
                abort(422)
    '''
  @TODO:
  Create a GET endpoint to get questions based on category.

  TEST: In the "List" tab / main screen, clicking on one of the
  categories in the left column will cause only questions of that
  category to be shown.
  '''
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_cat_questions(category_id):
        questions = Question.query.filter(Question.category == category_id).order_by(
            Question.category, Question.id).all()
        categories = Question.query.order_by(
            Question.category, Question.id).with_entities(Question.category).all()

        lcategory = list(set([Category.query.filter_by(
            id=item.category).one_or_none() for item in categories]))
        fcats = {cat.id: cat.type for cat in lcategory}
        if len(questions) == 0:
            return abort(404)
        else:
            prepared_questions = prepare_questions(
                request, questions, fcats)
            return prepared_questions
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
    @ app.route('/quizzes', methods=['POST'])
    def get_quiz():
        body = request.get_json()
        if body is None:
            abort(400)
        else:
            previous_questions = body.get('previous_questions', [])
            quiz_category = body.get('quiz_category', None)
            questions = Question.query.filter(
                not_(Question.id.in_(previous_questions))).all()
            if len(questions) == 0:
                abort(404)
            else:
                available_questions = [question.format()
                                       for question in questions]
                next_question = random.choice(available_questions)
                return jsonify({
                    'success': True,
                    'question': next_question
                })

    '''
  @TODO:
  Create error handlers for all expected errors
  including 404 and 422.
  '''
    @ app.errorhandler(404)
    def error_404(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }),404

    @ app.errorhandler(422)
    def error_422(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Unprocessable Entity'
        }),422

    @ app.errorhandler(400)
    def error_400(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }),400
    return app
