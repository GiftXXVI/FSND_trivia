import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "postgres", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {'question': 'In what state of matter are atoms most tightly packed?',
                             'answer': 'Solid', 'category': '1', 'difficulty': '2'}
        self.bad_cat_question = {'question': 'What is the nearest planet to the sun?',
                                 'answer': 'Mercury', 'category': '100', 'difficulty': '2'}
        self.bad_question = {
            'question': 'Which of Newton\'s laws states that for every action, there\'s and equal and opposite reaction?', 'answer': 'The third law of motion'}

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        cats = Category.query.count()

        if cats > 0:
            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)

            # test response body
            self.assertEqual(data['success'], False)
            self.assertNotIn('categories', data.keys())
            self.assertEqual(data['message'], 'Not Found')

    def test_get_paginated_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        qns = Question.query.count()

        if qns > 0:
            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertIn('num_pages', data.keys())
            self.assertIn('totalQuestions', data.keys())
            self.assertIn('questions', data.keys())
            self.assertIn('currentCategory', data.keys())
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('totalQuestions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('currentCategory', data.keys())
            self.assertNotIn('categories', data.keys())

    def test_get_paginated_questions_high_page_num(self):
        response = self.client().get('/questions?page=2000000000000000')
        data = json.loads(response.data)

        qns = Question.query.count()

        if qns > 0:
            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertIn('num_pages', data.keys())
            self.assertIn('totalQuestions', data.keys())
            self.assertIn('questions', data.keys())
            self.assertIn('currentCategory', data.keys())
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('totalQuestions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('currentCategory', data.keys())
            self.assertNotIn('categories', data.keys())

    def test_get_paginated_questions_low_page_num(self):
        response = self.client().get('/questions?page=0')
        data = json.loads(response.data)

        qns = Question.query.count()

        if qns > 0:
            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertIn('num_pages', data.keys())
            self.assertIn('totalQuestions', data.keys())
            self.assertIn('questions', data.keys())
            self.assertIn('currentCategory', data.keys())
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('totalQuestions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('currentCategory', data.keys())
            self.assertNotIn('categories', data.keys())

    def test_get_paginated_questions_decimal_page_num(self):
        response = self.client().get('/questions?page=1.53')
        data = json.loads(response.data)

        qns = Question.query.count()

        if qns > 0:

            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertIn('num_pages', data.keys())
            self.assertIn('totalQuestions', data.keys())
            self.assertIn('questions', data.keys())
            self.assertIn('currentCategory', data.keys())
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                len([e for e in data['categories'] if list(data['categories']).count(e) > 1]), 0)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('totalQuestions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('currentCategory', data.keys())
            self.assertNotIn('categories', data.keys())

    def test_create_question(self):
        response = self.client().post('/questions', json=self.new_question)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertEqual(data['success'], True)
        self.assertIn('created', data.keys())

    def test_create_question_empty_body(self):
        response = self.client().post('/questions')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 400)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertNotIn('created', data.keys())
        self.assertEqual(data['message'], 'Bad Request')

    def test_create_question_invalid_category(self):
        response = self.client().post('/questions', json=self.bad_cat_question)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 422)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertNotIn('created', data.keys())
        self.assertEqual(data['message'], 'Unprocessable Entity')

    def test_create_question_missing_fields(self):
        response = self.client().post('/questions', json=self.bad_question)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 400)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertNotIn('created', data.keys())
        self.assertEqual(data['message'], 'Bad Request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
