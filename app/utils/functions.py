from flask import jsonify


def create_http_response(message: str, status: str, http_status: int, result: dict = None):
    if result is None:
        result = {}
    response = {
        'message': message,
        'status': status,
        'result': result
    }
    return jsonify(response), http_status
