from ..models.blog_post import BlogPost, db
from ..models.user import User
from ..models.topic import Topic
from ..utils.functions import create_http_response
from flask import Response
from ..utils.validations import input_validation
from ..services.auth import authentication_required
from werkzeug.exceptions import NotFound


def get_all_blogs() -> tuple[Response, int]:
    try:
        blogs = db.session.execute(db.select(BlogPost)).scalars().all()
        return create_http_response(result=blogs, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


def get_blog(blog_id: int) -> tuple[Response, int]:
    try:
        blog = db.session.execute(db.select(BlogPost).where(BlogPost.id == blog_id)).scalar().to_dict()
        return create_http_response(result=blog, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


@authentication_required
@input_validation(
    title={"required": True, "min_length": 5},
    body={"required": True},
    topic_ids={"array": True}
)
def create_blog(request_data: dict, user_id: int = None) -> tuple[Response, int]:
    title = request_data.get("title")
    body = request_data.get("body")
    priority = request_data.get("priority")
    topic_ids = request_data.get("topic_ids")

    already_existing_title = db.session.execute(db.select(BlogPost).where(BlogPost.title == title)).scalar()
    if already_existing_title:
        return create_http_response(message='already blog with that title', status='failed', http_status=400)

    author = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    if not author:
        return create_http_response(message="No user found with that token", status='failed', http_status=401)

    new_blog = BlogPost(
        title=title,
        body=body,
        author=author,
    )

    if priority:
        new_blog.priority = priority

    if topic_ids:
        topics = [db.session.execute(db.select(Topic).where(Topic.id == topic_id)).scalar() for topic_id in topic_ids]
        if None in topics:
            return create_http_response(message="Topic id not found", status='failed', http_status=404)
        new_blog.topics = topics

    db.session.add(new_blog)
    db.session.commit()

    return create_http_response(
        message='Successfully blogged',
        status='success',
        http_status=201
    )


@authentication_required
@input_validation(
    blog_id={"required": True},
    title={"required": True, "min_length": 5},
    body={"required": True},
    topic_ids={"array": True}
)
def update_blog(request_data: dict, blog_id: int,  user_id: int = None) -> tuple[Response, int]:
    try:
        blog = db.session.execute(db.select(BlogPost).filter_by(id=blog_id, author_id=user_id)).scalar()
        if not blog:
            raise NotFound

        title = request_data.get("title")
        body = request_data.get("body")
        priority = request_data.get("priority")
        topic_ids = request_data.get("topic_ids")

        already_existing_title = db.session.execute(db.select(BlogPost).where(
            BlogPost.title == title, BlogPost.id != blog_id
        )).scalar()
        if already_existing_title:
            return create_http_response(message='already blog with that title', status='failed', http_status=400)

        author = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
        if not author:
            return create_http_response(message="No user found with that token", status='failed', http_status=401)

        updated_blog = {
            "title": title,
            "body": body,
            "author": author
        }

        if priority:
            updated_blog["priority"] = priority

        if topic_ids:
            topics = [db.session.execute(db.select(Topic).where(Topic.id == topic_id)).scalar() for topic_id in
                      topic_ids]
            if None in topics:
                return create_http_response(message="Topic id not found", status='failed', http_status=404)
            updated_blog["topics"] = topics

        blog.title = updated_blog["title"]
        blog.body = updated_blog["body"]
        if priority:
            blog.priority = updated_blog["priority"]
        if topic_ids:
            blog.topics = updated_blog["topics"]
        db.session.commit()

    except NotFound:
        return create_http_response(message=f"Blog id {blog_id} not found", status="failed", http_status=404)
    except Exception as e:
        db.session.rollback()
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


@authentication_required
def delete_blog(blog_id, user_id: int = None):
    try:
        blog = db.session.execute(db.select(BlogPost).filter_by(id=blog_id, author_id=user_id)).scalar()
        if not blog:
            raise NotFound
        db.session.delete(blog)
        db.session.commit()
        return create_http_response(message='Successfully deleted', status='success', http_status=204)
    except NotFound:
        return create_http_response(message=f"Blog id {blog_id} not found", status="failed", http_status=404)
    except Exception as e:
        db.session.rollback()
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)
