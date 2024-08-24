from app.main_blueprint import bp
from flask import request

@bp.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"