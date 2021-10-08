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

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response)

        #test response code
        self.assertEqual(response.status_code, 200)
        
        #test response body
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len([e for e in data['categories'] if data['categories'].count(e) > 1]),0)
        self.assertTrue(data['page_num'])
        self.assertTrue(data['curr_page_size'])
        self.assertTrue(data['num_pages'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(data['categories'])        
    
    def test_get_paginated_questions_high_page_num(self):
        response = self.client().get('/questions?page=2000000000000000')
        data = json.loads(response)

        #test response code
        self.assertEqual(response.status_code, 200)

        #test response body
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len([e for e in data['categories'] if data['categories'].count(e) > 1]),0)
        self.assertTrue(data['page_num'])
        self.assertTrue(data['curr_page_size'])
        self.assertTrue(data['num_pages'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(data['categories'])  
    
    def test_get_paginated_questions_low_page_num(self):
        response = self.client().get('/questions?page=0')
        data = json.loads(response)

        #test response code
        self.assertEqual(response.status_code, 200)

        #test response body
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len([e for e in data['categories'] if data['categories'].count(e) > 1]),0)
        self.assertTrue(data['page_num'])
        self.assertTrue(data['curr_page_size'])
        self.assertTrue(data['num_pages'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(data['categories'])  

    def test_get_paginated_questions_decimal_page_num(self):
        response = self.client().get('/questions?page=1.53')
        data = json.loads(response)

        #test response code
        self.assertEqual(response.status_code, 200)

        #test response body
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len([e for e in data['categories'] if data['categories'].count(e) > 1]),0)
        self.assertTrue(data['page_num'])
        self.assertTrue(data['curr_page_size'])
        self.assertTrue(data['num_pages'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(data['categories'])  
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
