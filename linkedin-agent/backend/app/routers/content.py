from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Post, OAuthToken
from ..schemas import (
    StrategyRequest, StrategyResponse, StrategyItem,
    GenerateRequest, GenerateResponse,
    OptimizeRequest, OptimizeResponse,
    ScheduleRequest, CalendarItem,
)
from ..services.llm import generate_strategy, generate_content as llm_generate_content, optimize_content as llm_optimize_content
from ..services.scheduler import schedule_post

router = APIRouter(prefix="/api/content", tags=["content"]) 


@router.post("/strategy", response_model=StrategyResponse)
async def strategy(req: StrategyRequest):
    pillars, cal = generate_strategy(req.industry, req.role, req.interests, req.frequency_per_week)
    calendar = [StrategyItem(date=datetime.fromisoformat(i["date"]), post_type=i["post_type"], topic=i["topic"]) for i in cal]
    return StrategyResponse(pillars=pillars, calendar=calendar)


@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    content, hashtags = llm_generate_content(req.post_type, req.prompt, req.language or "en")
    return GenerateResponse(content=content, hashtags=hashtags, metadata={"post_type": req.post_type})


@router.post("/optimize", response_model=OptimizeResponse)
async def optimize(req: OptimizeRequest):
    improved, hashtags, suggestions = llm_optimize_content(req.content)
    return OptimizeResponse(content=improved, hashtags=hashtags, suggestions=suggestions)


@router.post("/schedule", response_model=CalendarItem)
async def schedule(req: ScheduleRequest, db: Session = Depends(get_db)):
    user_id = 1  # demo
    post = Post(user_id=user_id, type=req.post_type, content=req.content, status="scheduled", scheduled_at=req.scheduled_at)
    db.add(post)
    db.commit()
    db.refresh(post)

    schedule_post(post.id, req.scheduled_at)

    return CalendarItem(id=post.id, content=post.content, post_type=post.type, status=post.status, scheduled_at=post.scheduled_at)


@router.get("/calendar", response_model=list[CalendarItem])
async def calendar(db: Session = Depends(get_db)):
    posts = db.query(Post).order_by(Post.scheduled_at.desc().nullslast()).all()
    return [CalendarItem(id=p.id, content=p.content, post_type=p.type, status=p.status, scheduled_at=p.scheduled_at) for p in posts]