from flask import Blueprint, request
from ..utils.decorators import require_json
from ..services.comment import comments_from_blog, create_comment

comment_blueprint = Blueprint('comment_blueprint ', __name__)


@comment_blueprint.route("/comment/blog/<int:blog_id>", methods=['GET', 'POST'])
@require_json(methods=['POST'])
def comments(blog_id: int):
    if request.method == 'GET':
        return comments_from_blog(blog_id)
    if request.method == 'POST':
        return create_comment(request_data=request.get_json(), blog_id=blog_id)

