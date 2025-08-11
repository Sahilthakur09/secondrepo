from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()


class CalendarItem(BaseModel):
    id: str
    scheduled_time: datetime
    content_preview: str
    status: str


@router.get("/", response_model=List[CalendarItem])
async def list_calendar() -> List[CalendarItem]:
    return [
        CalendarItem(
            id="1",
            scheduled_time=datetime.utcnow(),
            content_preview="5 tips to accelerate your career in data science...",
            status="scheduled",
        )
    ]