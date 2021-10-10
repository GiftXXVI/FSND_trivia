from flask import jsonify
from math import ceil

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
        'total_questions': length_questions,
        'questions': paginated_questions,
        'current_category': curr_cat,
        'categories': lcategory
    })