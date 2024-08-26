from typing import Callable
from functools import wraps
from flask import request, jsonify
import json


def require_json(f: Callable) -> Callable:
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "No data provided"}), 400

        try:
            data = request.get_json()
            if data is None:
                return jsonify({"message": "Empty JSON body"}), 400
        except json.JSONDecodeError as e:
            return jsonify({"message": f"Invalid JSON format: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"message": f"An unexpected error occurred: {str(e)}"}), 500

        return f(*args, **kwargs)

    return decorated_function
