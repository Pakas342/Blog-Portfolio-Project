from app.blueprints import *
from flask import Flask


def add_blueprints(app: Flask):
    app.register_blueprint(hello_world_blueprint)
