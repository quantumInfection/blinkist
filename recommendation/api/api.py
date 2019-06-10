"""
This module contains blueprints for api request for recommendations. All recommendations requests
will go through here
"""

from flask import Blueprint, request
from utils import verify_args, serialize
from recommendation.repo import get_book_selection_a, get_book_selection_b

rec_app = Blueprint('rec_app', __name__, url_prefix='/recommendations/v1')


@rec_app.route('/books-a')
@verify_args(['user_id'])
@serialize
def books_a():
    """
    This method will get books from selection A from repo against a user id

    Request:
        - user_id: str (Required)

    Response:
        - book_ids: List[selection]

    Where a selection is:
        - selector: str, a or a+b
        - book_id: str
    """
    args = request.args
    return {'book_ids': get_book_selection_a(user_id=args['user_id'])}


@rec_app.route('/books-b')
@serialize
def books_b():
    """
    This method will get books from selection B from repo against a user id

    Request:
        - user_id: str (Required)

    Response:
        - book_ids: List[selection]

    Where a selection is:
        - selector: str, a or a+b
        - book_id: str
    """
    args = request.args
    return {'book_ids': get_book_selection_b(user_id=args['user_id'])}
