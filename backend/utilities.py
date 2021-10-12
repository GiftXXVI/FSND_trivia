from flask import jsonify
from math import ceil
from models import Question

QUESTIONS_PER_PAGE = 10


def paginate_questions(page, questions):
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    pquestions = Question.query.order_by(Question.category, Question.id).limit(
        QUESTIONS_PER_PAGE).offset(start).all()
    fquestions = [question.format() for question in pquestions]
    lquestions = len(fquestions)
    npages = ceil(questions/QUESTIONS_PER_PAGE)

    return fquestions, lquestions, npages


def prepare_questions(request, questions, lcategory):
    page = request.args.get('page', 1, type=int)
    paginated_questions, page_size, num_pages = paginate_questions(
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
        'total_questions': questions,
        'questions': paginated_questions,
        'current_category': curr_cat,
        'categories': lcategory
    })
