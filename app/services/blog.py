from ..models.blog_post import BlogPost, db
from ..utils.functions import create_http_response


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
