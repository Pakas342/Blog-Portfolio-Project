from .auth import auth_blueprint
from .blog import blog_blueprint
from .topic import topic_blueprint
from .comment import comment_blueprint

__all__ = ["auth_blueprint", "blog_blueprint", "topic_blueprint", "comment_blueprint"]
