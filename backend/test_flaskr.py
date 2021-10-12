import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from random import choice


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.getenv("TEST_NAME")
        self.database_user = os.getenv("TEST_USER")
        self.database_password = os.getenv("TEST_PASS")
        self.database_host = os.getenv("TEST_HOST")
        self.database_port = os.getenv("TEST_PORT")
        self.database_host_port = f"{self.database_host}:{self.database_port}"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            self.database_user, self.database_password, self.database_host_port, self.database_name
        )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {'question': 'In what state of matter are atoms most tightly packed?',
                             'answer': 'Solid', 'category': '1', 'difficulty': '2', "rating": 2}
        self.bad_cat_question = {'question': 'What is the nearest planet to the sun?',
                                 'answer': 'Mercury', 'category': '100', 'difficulty': '2', "rating": 2}
        self.bad_question = {
            'question': 'Which of Newton\'s laws states that for every action, there\'s and equal and opposite reaction?', 'answer': 'The third law of motion'}
        self.valid_search = {'searchTerm': 'India'}
        self.invalid_search = {'searchTerm': '###'}

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

    def test_create_category(self):
        response = self.client().post('/categories', json={"type": "Food"})
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertEqual(data['success'], True)
        self.assertIn('created', data.keys())

    def test_create_category_empty_body(self):
        response = self.client().post('/categories')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 400)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertNotIn('created', data.keys())
        self.assertEqual(data['message'], 'Bad Request')

    def test_get_paginated_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        qns = Question.query.count()

        if qns > 0:
            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertIn('num_pages', data.keys())
            self.assertIn('total_questions', data.keys())
            self.assertIn('questions', data.keys())
            self.assertIn('current_category', data.keys())
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('total_questions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('current_category', data.keys())
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
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertEqual(data['curr_page_size'], 0)
            self.assertIn('num_pages', data.keys())
            self.assertGreater(data['num_pages'], 0)
            self.assertIn('total_questions', data.keys())
            self.assertGreater(data['total_questions'], 0)
            self.assertIn('questions', data.keys())
            self.assertEqual(len(data['questions']), 0)
            self.assertIn('current_category', data.keys())
            self.assertFalse(data['current_category'])
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('total_questions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('current_category', data.keys())
            self.assertNotIn('categories', data.keys())

    def test_get_paginated_questions_low_page_num(self):
        response = self.client().get('/questions?page=-20')
        data = json.loads(response.data)

        qns = Question.query.count()

        if qns > 0:
            # test response code
            self.assertEqual(response.status_code, 200)

            # test response body
            self.assertEqual(data['success'], True)
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertEqual(data['curr_page_size'], 0)
            self.assertIn('num_pages', data.keys())
            self.assertGreater(data['num_pages'], 0)
            self.assertIn('total_questions', data.keys())
            self.assertGreater(data['total_questions'], 0)
            self.assertIn('questions', data.keys())
            self.assertEqual(len(data['questions']), 0)
            self.assertIn('current_category', data.keys())
            self.assertFalse(data['current_category'])
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('total_questions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('current_category', data.keys())
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
            self.assertIn('page_num', data.keys())
            self.assertIn('curr_page_size', data.keys())
            self.assertGreaterEqual(data['curr_page_size'], 0)
            self.assertIn('num_pages', data.keys())
            self.assertGreater(data['num_pages'], 0)
            self.assertIn('total_questions', data.keys())
            self.assertGreaterEqual(data['total_questions'], 0)
            self.assertIn('questions', data.keys())
            self.assertGreaterEqual(len(data['questions']), 0)
            self.assertIn('current_category', data.keys())
            self.assertIn('categories', data.keys())
        else:
            # test response code
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertNotIn('page_num', data.keys())
            self.assertNotIn('curr_page_size', data.keys())
            self.assertNotIn('num_pages', data.keys())
            self.assertNotIn('total_questions', data.keys())
            self.assertNotIn('questions', data.keys())
            self.assertNotIn('current_category', data.keys())
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

    def test_delete_question(self):
        latest = Question.query.order_by(self.db.desc(Question.id)).first()
        response = self.client().delete(f'/questions/{latest.id}')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], latest.id)

    def test_delete_question_no_id(self):
        response = self.client().delete('/questions')
        data = json.loads(response.data)

        # test reponse code
        self.assertEqual(response.status_code, 405)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_delete_question_invalid_id(self):
        response = self.client().delete('/questions/-2')
        data = json.loads(response.data)

        # test reponse code
        self.assertEqual(response.status_code, 404)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_search_questions(self):
        response = self.client().post('/questions/search', json=self.valid_search)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertEqual(data['success'], True)
        self.assertIn('page_num', data.keys())
        self.assertIn('curr_page_size', data.keys())
        self.assertIn('num_pages', data.keys())
        self.assertIn('total_questions', data.keys())
        self.assertIn('questions', data.keys())
        self.assertIn('current_category', data.keys())
        self.assertIn('categories', data.keys())

    def test_search_questions_invalid(self):
        response = self.client().post('/questions/search', json=self.invalid_search)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertEqual(data['success'], True)
        self.assertIn('page_num', data.keys())
        self.assertIn('curr_page_size', data.keys())
        self.assertIn('num_pages', data.keys())
        self.assertIn('total_questions', data.keys())
        self.assertIn('questions', data.keys())
        self.assertIn('current_category', data.keys())
        self.assertIn('categories', data.keys())

    def test_search_questions_empty(self):
        response = self.client().post('/questions/search')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 400)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertNotIn('page_num', data.keys())
        self.assertNotIn('curr_page_size', data.keys())
        self.assertNotIn('num_pages', data.keys())
        self.assertNotIn('total_questions', data.keys())
        self.assertNotIn('questions', data.keys())
        self.assertNotIn('current_category', data.keys())
        self.assertNotIn('categories', data.keys())

    def test_get_category_questions(self):
        categories = Category.query.join('questions').order_by(Category.id).all()
        rand = choice([cat.id for cat in categories])
        response = self.client().get(f'/categories/{rand}/questions')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertEqual(data['success'], True)
        self.assertIn('page_num', data.keys())
        self.assertIn('curr_page_size', data.keys())
        self.assertIn('num_pages', data.keys())
        self.assertIn('total_questions', data.keys())
        self.assertIn('questions', data.keys())
        self.assertIn('current_category', data.keys())
        self.assertIn('categories', data.keys())

    def test_get_category_questions_invalid_category(self):
        response = self.client().get('/categories/-2/questions')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 404)

        # test response body
        self.assertEqual(data['success'], False)
        self.assertNotIn('page_num', data.keys())
        self.assertNotIn('curr_page_size', data.keys())
        self.assertNotIn('num_pages', data.keys())
        self.assertNotIn('total_questions', data.keys())
        self.assertNotIn('questions', data.keys())
        self.assertNotIn('current_category', data.keys())
        self.assertNotIn('categories', data.keys())

    def test_get_quizzes(self):
        categories = Category.query.join('questions').order_by(Category.id).all()
        rand_cat = choice([cat.id for cat in categories])

        questions = Question.query.filter(
            Question.category == rand_cat).order_by(Question.id).all()
        rand_question = choice([question.id for question in questions])

        request_data = {'previous_questions': [
            rand_question], 'quiz_category': {'id': rand_cat}}

        response = self.client().post('/quizzes', json=request_data)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 200)

        # test response body
        self.assertIn('question', data.keys())

    def test_get_quizzes_empty(self):
        response = self.client().post('/quizzes')
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 400)

        # test response body
        self.assertNotIn('question', data.keys())

    def test_get_quizzes_no_category(self):
        req_data = {}
        response = self.client().post('/quizzes', json=req_data)
        data = json.loads(response.data)

        # test response code
        self.assertEqual(response.status_code, 422)

        # test response body
        self.assertNotIn('question', data.keys())


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
