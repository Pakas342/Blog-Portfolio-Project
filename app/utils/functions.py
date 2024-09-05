from flask import jsonify


def create_http_response(
    status: str,
    http_status: int,
    message: str = None,
    result: dict = None,
    auth_token: str = None
) -> tuple:
    response = {'status': status}

    if message:
        response['message'] = message

    if result:
        response['result'] = result
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
