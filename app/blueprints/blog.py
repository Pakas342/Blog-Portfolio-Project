from flask import Blueprint, request
from ..utils.decorators import require_json
from ..services.blog import get_blog, get_all_blogs, create_blog, delete_blog, update_blog, get_blogs_by_topic

blog_blueprint = Blueprint('blog_blueprint ', __name__)


@blog_blueprint.route("/blog", methods=['GET', 'POST'])
@require_json(methods=['POST'])
def blogs():
    if request.method == 'POST':
        return create_blog(request_data=request.get_json())
    return get_all_blogs()


@blog_blueprint.route("/blog/<int:blog_id>", methods=['GET', 'PUT', 'DELETE'])
@require_json(methods=['PUT'])
def unique_blog(blog_id: int):
    if request.method == 'GET':
        return get_blog(blog_id)
    if request.method == 'PUT':
        return update_blog(request_data=request.get_json())
    if request.method == 'DELETE':
        return delete_blog(blog_id)


@blog_blueprint.route("/blog/topic/<int:topic_id>")
def blogs_per_topic(topic_id: int):
    return get_blogs_by_topic(topic_id)
