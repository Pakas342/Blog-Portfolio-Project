from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, DateTime
from typing import List
from datetime import datetime
from app.models import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog_post import BlogPost

class Topic(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    blog_posts: Mapped[List["BlogPost"]] = relationship(secondary="blog_post_topic", back_populates="topics")
    
#join table fro Topics and Blog Posts
class BlogPostTopic(db.Model):
    blog_post_id: Mapped[int] = mapped_column(ForeignKey('blog_post.id'), primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey('topic.id'), primary_key=True)
    
