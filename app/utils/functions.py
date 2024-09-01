from flask import jsonify


def create_http_response(
    message: str, status: str,
        http_status: int,
        result: dict = None,
        auth_token: str = None
                        ) -> tuple:
    if result is None:
        response = {
            'message': message,
            'status': status,
        }
    else:
        response = {
            'message': message,
            'status': status,
            'result': result
        }

    resp = jsonify(response)

    if auth_token:
        resp.set_cookie(
            'auth_token',
            auth_token,
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=86400
        )

    return resp, http_status
