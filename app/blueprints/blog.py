from flask import Blueprint
from ..services.auth import authentication_required
from ..utils.decorators import require_json
from ..services.blog import get_blog, get_all_blogs

blog_blueprint = Blueprint('blog_blueprint ', __name__)


@blog_blueprint.route("/blog", methods=['GET'])
@require_json(methods=['POST'])
def get_blogs():
    return get_all_blogs()


@blog_blueprint.route("/blog/<int:blog_id>", methods=['GET', 'PUT', 'DELETE'])
@require_json(methods=['PUT'])
def get_blog_data(blog_id: int):
    return get_blog(blog_id)


