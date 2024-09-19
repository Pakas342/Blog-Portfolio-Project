from flask import Blueprint, request
from ..utils.decorators import require_json
from ..services.topic import get_topics, create_topic

topic_blueprint = Blueprint('blog_blueprint ', __name__)


@topic_blueprint.route("/topic", methods=['GET', 'POST'])
@require_json(methods=['POST'])
def topics():
    if request.method == 'POST':
        return create_topic(request.get_json())
    if request.method == 'GET':
        return get_topics()
