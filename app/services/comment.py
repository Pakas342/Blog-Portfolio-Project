from ..models.comment import Comment, db
from ..models.blog_post import BlogPost
from ..models.user import User
from ..utils.functions import create_http_response
from .auth import authentication_required
from ..utils.validations import input_validation
from flask import Response, request


def comments_from_blog(blog_id:int) -> tuple[Response, int]:
    try:
        blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == blog_id)).scalar().to_dict()
        comments = blog["comments"]
        return create_http_response(result=comments, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


@authentication_required
@input_validation(
    body={'required': True, "min_length": 2}
)
def create_comment(request_data:dict, blog_id: int, user_id: int = None) -> tuple[Response, int]:
    body = request_data.get('body')
    blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == blog_id)).scalar()
    author = db.session.execute(db.select(User).where(User.id == user_id)).scalar()

    if not author:
        return create_http_response(message="No user found with that token", status='failed', http_status=401)

    new_comment = Comment(
        body=body,
        blog=blog,
        author=author
    )
    db.session.add(new_comment)
    db.session.execute()
