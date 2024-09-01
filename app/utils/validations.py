import re
from typing import Union
from .functions import create_http_response
from functools import wraps


def input_validation(**expected_fields: dict) -> callable:
    def decorator(f):
        @wraps(f)
        def decorated_function(request_data: dict):
            for field, validations in expected_fields.items():
                value = request_data.get(field)

                if 'required' in validations and not value:
                    return create_http_response(f'{field} is required', 'failed', 400)

                if 'min_length' in validations and len(value) < validations['min_length']:
                    return create_http_response(f"{field} must be at least {validations['min_length']} characters long",
                                                'failed',
                                                400
                                                )

                if 'email' in validations and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                    return create_http_response(f'Invalid email format for {field}', 'failed', 400)

            return f(request_data)
        return decorated_function
    return decorator
