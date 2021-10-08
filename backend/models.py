import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "trivia"
database_path = "postgresql://{}:{}@{}/{}".format(
    "postgres", "postgres", "localhost:5432", database_name
)

# flask db init
# flask db migrate -m "Add relationship between question and category."
# UPDATE question AS q SET q.category_id=(SELECT c.id FROM category AS c WHERE c.type=q.category LIMIT 1)
#op.execute('UPDATE question AS q SET q.category_id=(SELECT c.id FROM category AS c WHERE c.type=q.category LIMIT 1)')
#op.drop_column('question', 'category')
# flask db upgrade

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def get_db():
    return db


'''
Question

'''


class Question(db.Model):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
        }
    
    def rollback():
        db.session.rollback()
        
    def refresh(self):
        db.session.refresh(self)

    def dispose(self):
        db.session.close()


'''
Category

'''


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def rollback():
        db.session.rollback()

    def refresh():
        db.session.refresh(self)

    def dispose(self):
        db.session.close()
