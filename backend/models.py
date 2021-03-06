import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy.sql.schema import ForeignKey

database_name = os.getenv("DB_NAME")
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASS")
database_host = os.getenv("DB_HOST")
database_port = os.getenv("DB_PORT")
database_host_port = f"{database_host}:{database_port}"
database_path = "postgresql://{}:{}@{}/{}".format(
    database_user, database_password, database_host_port, database_name
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
    category = Column(Integer, ForeignKey('categories.id'), nullable=False)
    difficulty = Column(Integer)
    rating = Column(Integer)

    def __init__(self, question, answer, category, difficulty, rating):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty
        self.rating = rating

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
            'difficulty': self.difficulty,
            'rating': self.rating
        }

    def rollback(self):
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
    questions = db.relationship('Question', backref='cat', lazy=True)

    def __init__(self, type):
        self.type = type

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def refresh(self):
        db.session.refresh(self)

    def dispose(self):
        db.session.close()
