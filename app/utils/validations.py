import re
from typing import Union

from .functions import create_http_response


class UserInputsValidation:

    @staticmethod
    def email_validation(email: str) -> Union[None, dict]:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return create_http_response('Invalid email format', 'failed', 400)

    @staticmethod
    def password_validation(password: str) -> Union[None, dict]:
        if len(password) < 8:
            return create_http_response('Password must be at least 8 characters long', 'failed', 400)

    @staticmethod
    def validate_existence(*args: Union[str, int]) -> Union[None, dict]:
        for user_input in args:
            if not user_input:
                return create_http_response(f'{user_input} is required', 'failed', 400)
