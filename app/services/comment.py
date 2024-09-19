from ..models.comment import Comment, db
from ..models.blog_post import BlogPost
from ..utils.functions import create_http_response
from .auth import authentication_required
from ..utils.validations import input_validation
from flask import Response


def comments_from_blog(blog_id:int) -> tuple[Response, int]:
    try:
        blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == blog_id)).scalar().to_dict()
        comments = blog["comments"]
        return create_http_response(result=comments, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


@authentication_required
def create_comment(blog_id:int, user_id: int = None) -> tuple[Response, int]:
    pass


