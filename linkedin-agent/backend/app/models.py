from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    linkedin_id = Column(String(128), unique=True, index=True, nullable=True)
    email = Column(String(256), index=True, nullable=True)
    full_name = Column(String(256), nullable=True)
    headline = Column(String(512), nullable=True)
    about = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")
    tokens = relationship("OAuthToken", back_populates="user", cascade="all, delete-orphan", uselist=False)


class OAuthToken(Base):
    __tablename__ = "oauth_tokens"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    provider = Column(String(64), default="linkedin")
    access_token = Column(Text, nullable=True)
    refresh_token = Column(Text, nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="tokens")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)

    type = Column(String(32), nullable=False)  # text, carousel, article, poll
    content = Column(Text, nullable=False)
    metadata = Column(JSON, nullable=True)

    status = Column(String(32), default="draft")  # draft, scheduled, published, failed
    scheduled_at = Column(DateTime(timezone=True), nullable=True)
    published_at = Column(DateTime(timezone=True), nullable=True)
    platform_post_id = Column(String(256), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="posts")
    analytics = relationship("Analytics", back_populates="post", cascade="all, delete-orphan")


class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), index=True, nullable=False)

    impressions = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    shares = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    post = relationship("Post", back_populates="analytics")