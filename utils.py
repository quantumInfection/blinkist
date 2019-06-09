"""This module contains all the utility functions"""

from functools import wraps
from flask import request
import json


def verify_args(required_fields=None):
    """Wrapper of Decorator to pass arguments"""
    def decorator(func):
        """Checks if all the args exist in payload."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper to execute the function"""
            def is_invalid(reqt):
                if reqt is None:
                    return True
                return required_fields and not all([rf in reqt for rf in required_fields])

            req = request.get_json()
            if request.method == 'GET':
                req = set(request.args.keys())
            if is_invalid(req):
                return 'Bad request', 400

            return func(*args, **kwargs)
        return wrapper
    return decorator


def serialize(func):
    """Decorator to serialize an object."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper
