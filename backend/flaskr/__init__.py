from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from categories_blueprint import categories_blueprint
from questions_blueprint import questions_blueprint
from quizzes_blueprint import quizzes_blueprint
from models import setup_db, Question, Category, get_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(questions_blueprint)
    app.register_blueprint(quizzes_blueprint)
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
  Create error handlers for all expected errors
  including 404 and 422.
  '''
    @ app.errorhandler(404)
    def error_404(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @ app.errorhandler(422)
    def error_422(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        }), 422

    @ app.errorhandler(400)
    def error_400(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400

    @ app.errorhandler(405)
    def error_405(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405

    @ app.errorhandler(500)
    def error_500(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500
    return app
