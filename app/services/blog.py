from ..models.blog_post import BlogPost, db
from ..utils.functions import create_http_response
from flask import jsonify
from ..utils.validations import input_validation


def get_all_blogs():
    try:
        blogs = db.session.execute(db.select(BlogPost)).scalars().all()
        return create_http_response(result=blogs, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


def get_blog(blog_id: int):
    try:
        blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == blog_id)).scalar
        return create_http_response(result=blog, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)

@input_validation(
    title={"required": True, "min_length": 5},
    body={"required": True}
)
def create_blog(request_data: dict) -> jsonify:
    pass