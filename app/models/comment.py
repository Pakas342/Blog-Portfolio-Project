from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, Text, ForeignKey, DateTime
from datetime import datetime
from app.models import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .blog_post import BlogPost


class Comment(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    blog_id: Mapped[int] = mapped_column(ForeignKey("blog_post.id"))
    blog: Mapped["BlogPost"] = relationship(back_populates="comments")
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="comments")
    
