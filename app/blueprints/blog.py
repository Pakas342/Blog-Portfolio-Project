from flask import Blueprint, request
from ..utils.decorators import require_json
from ..services.blog import get_blog, get_all_blogs, create_blog, delete_blog

blog_blueprint = Blueprint('blog_blueprint ', __name__)


@blog_blueprint.route("/blog", methods=['GET', 'POST'])
@require_json(methods=['POST'])
def get_blogs():
    if request.method == 'POST':
        return create_blog(request.get_json())
    return get_all_blogs()


@blog_blueprint.route("/blog/<int:blog_id>", methods=['GET', 'PUT', 'DELETE'])
@require_json(methods=['PUT'])
def get_blog_data(blog_id: int):
    if request.method == 'DELETE':
        return delete_blog(blog_id)
    return get_blog(blog_id)
