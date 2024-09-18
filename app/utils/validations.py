import re
from typing import Union
from .functions import create_http_response
from functools import wraps


def input_validation(**expected_fields: dict) -> callable:
    def decorator(f):
        @wraps(f)
        def decorated_function(request_data: dict, *args, **kwargs):
            for field, validations in expected_fields.items():
                value = request_data.get(field)

                if 'required' in validations and not value:
                    return create_http_response(message=f'{field} is required', status='failed', http_status=400)

                if 'min_length' in validations and len(value) < validations['min_length']:
                    return create_http_response(
                        message=f"{field} must be at least {validations['min_length']} characters long",
                        status='failed',
                        http_status=400
                    )

                if 'array' in validations and value and not isinstance(value, list):
                    return create_http_response(
                        message=f'{field} is not an array',
                        status='failed',
                        http_status=400
                    )

                if 'email' in validations and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                    return create_http_response(
                        message=f'Invalid email format for {field}',
                        status='failed',
                        http_status=400
                    )
            return f(request_data, *args, **kwargs)

        return decorated_function

    return decorator
