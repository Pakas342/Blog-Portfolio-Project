from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime
from typing import List, TYPE_CHECKING
from datetime import datetime
from app.models import db
from sqlalchemy_serializer import SerializerMixin


if TYPE_CHECKING:
    from .user import User
    from .comment import Comment
    from .topic import Topic


class BlogPost(db.Model, SerializerMixin):
    __tablename__ = "blog_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="blog_posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="blog")
    priority: Mapped[int] = mapped_column(Integer, default=1)
    topics: Mapped[List["Topic"]] = relationship(secondary="blog_post_topic", back_populates="blog_posts")

    serialize_only = ('id', 'title', 'created_at', 'updated_at', 'body', 'author_id', 'priority')

    def to_dict(self, rules=(), **kwargs):
        data = super().to_dict(rules=rules, **kwargs)
        data['comments'] = [
            {
                'id': comment.id,
                'body': comment.body,
                'created_at': comment.created_at,
                'author_id': comment.author_id
            } for comment in self.comments
        ]
        data['topics'] = [
            {
                'id': topic.id,
                'name': topic.name
            } for topic in self.topics
        ]
        return data
