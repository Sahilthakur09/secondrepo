from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Post, Analytics as AnalyticsModel
from ..schemas import SummaryAnalytics, PostAnalytics, ABTestRequest, ABTestResponse

router = APIRouter(prefix="/api/analytics", tags=["analytics"]) 


@router.get("/summary", response_model=SummaryAnalytics)
async def summary(db: Session = Depends(get_db)):
    totals = db.query(
        func.count(Post.id),
        func.coalesce(func.sum(AnalyticsModel.impressions), 0),
        func.coalesce(func.sum(AnalyticsModel.likes), 0),
        func.coalesce(func.sum(AnalyticsModel.comments), 0),
        func.coalesce(func.sum(AnalyticsModel.shares), 0),
    ).outerjoin(AnalyticsModel, AnalyticsModel.post_id == Post.id).one()
    return SummaryAnalytics(
        total_posts=totals[0] or 0,
        total_impressions=totals[1] or 0,
        total_likes=totals[2] or 0,
        total_comments=totals[3] or 0,
        total_shares=totals[4] or 0,
    )


@router.get("/posts", response_model=list[PostAnalytics])
async def per_post(db: Session = Depends(get_db)):
    rows = db.query(AnalyticsModel).order_by(AnalyticsModel.created_at.desc()).all()
    return [
        PostAnalytics(
            post_id=r.post_id,
            impressions=r.impressions,
            likes=r.likes,
            comments=r.comments,
            shares=r.shares,
            created_at=r.created_at,
        )
        for r in rows
    ]


@router.post("/abtest", response_model=ABTestResponse)
async def abtest(_: ABTestRequest):
    return ABTestResponse(test_id="demo-test", status="scheduled")