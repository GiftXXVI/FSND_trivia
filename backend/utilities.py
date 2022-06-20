from flask import jsonify
from math import ceil

from flask import request
from models import Question
import json

QUESTIONS_PER_PAGE = 10


def paginate_questions(page, questions, category_id):
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    body = None
    
    if len(request.data) > 0:
        body = request.get_json()
    
    if body is None:
        search_term = None
    else:
        search_term = body.get('searchTerm', None)
    
    if search_term is None:
        if category_id is None:
            pquestions = Question.query.order_by(Question.category, Question.id).limit(
                QUESTIONS_PER_PAGE).offset(start).all()
        else:
            pquestions = Question.query.filter(Question.category == category_id).order_by(Question.category, Question.id).limit(
                QUESTIONS_PER_PAGE).offset(start).all()
    else:
        fsearch = f'%{search_term}%'
        if category_id is None:
            pquestions = Question.query.filter(Question.question.ilike(
                fsearch)).order_by(Question.category, Question.id).all()
        else:
            pquestions = Question.query.filter(Question.question.ilike(
                fsearch), Question.category == category_id).order_by(Question.category, Question.id).all()

    fquestions = [question.format() for question in pquestions]
    lquestions = len(fquestions)
    npages = ceil(questions/QUESTIONS_PER_PAGE)

    return fquestions, lquestions, npages


def prepare_questions(request, questions, lcategory, category_id=None):
    page = abs(request.args.get('page', 1, type=int))
    paginated_questions, page_size, num_pages = paginate_questions(
        page, questions, category_id)
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
        'total_questions': questions,
        'questions': paginated_questions,
        'current_category': curr_cat,
        'categories': lcategory
    })
