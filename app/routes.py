from app.blueprints import *
from flask import Flask


def add_blueprints(app: Flask):
    app.register_blueprint(hello_world_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(topic_blueprint)
