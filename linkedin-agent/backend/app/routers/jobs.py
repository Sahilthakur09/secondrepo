from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Post, OAuthToken, Analytics
from ..services import linkedin

router = APIRouter(prefix="/api/jobs", tags=["jobs"]) 


@router.post("/sync_analytics")
async def sync_analytics(db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.platform_post_id.isnot(None)).all()
    tokens = db.query(OAuthToken).first()
    if not tokens:
        return {"updated": 0}
    updated = 0
    for post in posts:
        metrics = linkedin.fetch_post_metrics(tokens.access_token or "", post.platform_post_id or "")
        a = Analytics(post_id=post.id,
                      impressions=metrics.get("impressions", 0),
                      likes=metrics.get("likes", 0),
                      comments=metrics.get("comments", 0),
                      shares=metrics.get("shares", 0))
        db.add(a)
        updated += 1
    db.commit()
    return {"updated": updated}