from typing import Callable
from functools import wraps
from flask import request
import json
from ..utils.functions import create_http_response


def require_json(f: Callable) -> Callable:
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.data:
            return create_http_response(message='Bad request, no data provided', status='failed', http_status=400)

        try:
            data = request.get_json()
            if data is None:
                return create_http_response(message='Empty JSON body', status='failed', http_status=400)
        except json.JSONDecodeError as e:
            return create_http_response(message=f'Invalid JSON format: {str(e)}', status='failed', http_status=400)
        except Exception as e:
            return create_http_response(message=f'An unexpected error occurred: {str(e)}', status='failed', http_status=500)

        return f(*args, **kwargs)

    return decorated_function
