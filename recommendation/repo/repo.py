"""
This module is entry point for repository. In the future this repo will be able to get anything
from sql, server side cache or any source of data. Right now we'll hard code it on application layer
"""

# Hard-coded books for now
books = {
    'a': ['book1', 'book2', 'book3', 'book4', 'book5', 'book6', 'book7', 'book8', 'book9',
          'book10'],
    'b': ['book2', 'book7', 'book19', 'book9', 'book25', 'book35', 'book4', 'book5', 'book6',
          'book20'],
}


def get_book_selection_a(user_id: str):
    """
    Returns selection a against a user id
    :param user_id: Unique user id of a user
    :return:
    """
    return books['a']


def get_book_selection_b(user_id: str):
    """
    Returns selection b against a user id
    :param user_id: Unique user id of a user
    :return:
    """
    return books['b']
