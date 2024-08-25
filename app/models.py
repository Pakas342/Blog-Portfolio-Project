from app import db
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, Column
from typing import List
from datetime import datetime

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(254), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    blog_posts: Mapped[List["BlogPost"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    
class BlogPost(db.Model):
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
    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    blog_id: Mapped[int] = mapped_column(ForeignKey("blog_post.id"))
    blog: Mapped["BlogPost"] =  relationship(back_populates="comments")
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="comments")
    
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