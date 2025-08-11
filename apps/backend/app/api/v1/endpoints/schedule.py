from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ....core.db import SessionLocal
from ....models.schedule import ScheduledPost
from ....schemas.schedule import ScheduleCreate, ScheduleOut
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ScheduleOut)
async def schedule_post(payload: ScheduleCreate, db: Session = Depends(get_db)) -> ScheduleOut:
    sp = ScheduledPost(content_body=payload.content_body, scheduled_time=payload.scheduled_time, status="scheduled")
    db.add(sp)
    db.commit()
    db.refresh(sp)
    return sp


@router.get("/", response_model=List[ScheduleOut])
async def list_scheduled_posts(db: Session = Depends(get_db)) -> List[ScheduleOut]:
    return db.query(ScheduledPost).order_by(ScheduledPost.scheduled_time.desc()).all()