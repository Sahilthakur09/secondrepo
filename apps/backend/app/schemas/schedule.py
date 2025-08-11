from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ScheduleCreate(BaseModel):
    content_body: str
    scheduled_time: datetime


class ScheduleOut(BaseModel):
    id: str
    content_body: str
    scheduled_time: datetime
    status: str

    class Config:
        orm_mode = True