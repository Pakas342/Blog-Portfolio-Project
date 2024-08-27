from typing import Callable
from functools import wraps
from flask import request
import json
from ..utils.functions import create_response


def require_json(f: Callable) -> Callable:
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.data:
            return create_response('Bad request, no data provided', 'failed', 400)

        try:
            data = request.get_json()
            if data is None:
                return create_response('Empty JSON body', 'failed', 400)
        except json.JSONDecodeError as e:
            return create_response(f'Invalid JSON format: {str(e)}', 'failed', 400)
        except Exception as e:
            response = {
                'message': f'An unexpected error occurred: {str(e)}',
                'status': 'failed',
            }
            return create_response(f'An unexpected error occurred: {str(e)}', 'failed', 500)

        return f(*args, **kwargs)

    return decorated_function
