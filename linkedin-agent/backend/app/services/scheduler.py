from __future__ import annotations
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Post, OAuthToken
from . import linkedin

scheduler = BackgroundScheduler()


def _publish_post(post_id: int):
    db: Session = SessionLocal()
    try:
        post = db.get(Post, post_id)
        if not post:
            return
        tokens = db.query(OAuthToken).filter(OAuthToken.user_id == post.user_id).first()
        if not tokens or not tokens.access_token:
            post.status = "failed"
            db.commit()
            return
        platform_id, published_at = linkedin.create_post(tokens.access_token, post.content, post.type)
        post.status = "published"
        post.platform_post_id = platform_id
        post.published_at = published_at
        db.commit()
    finally:
        db.close()


def start_scheduler():
    if not scheduler.running:
        scheduler.start()


def schedule_post(post_id: int, when: datetime):
    scheduler.add_job(_publish_post, "date", run_date=when, args=[post_id], id=f"post-{post_id}")