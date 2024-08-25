from flask import Blueprint

hello_world_blueprint = Blueprint('hello_world_blueprint', __name__)

@hello_world_blueprint.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"