from flask import Blueprint, request
from ..utils.decorators import require_json
from ..services.topic import get_topics, create_topic

comment_blueprint = Blueprint('comment_blueprint ', __name__)
