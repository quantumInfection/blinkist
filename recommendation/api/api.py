"""
This module contains blueprints for api request for recommendations. All recommendations requests
will go through here
"""

from flask import Blueprint, request
from utils import verify_args
from recommendation.repo import get_book_selection_a, get_book_selection_b

rec_app = Blueprint('rec_app', __name__, url_prefix='/recommendations/v1')


@rec_app.route('/books-a')
@verify_args(['user_id'])
def books_a():
    """This method will get books from selection A from repo against a user id"""
    args = request.args
    return get_book_selection_a(user_id=args['user_id'])


@rec_app.route('/books-b')
def books_b():
    """This method will get books from selection B from repo against a user id"""
    args = request.args
    return get_book_selection_b(user_id=args['user_id'])
