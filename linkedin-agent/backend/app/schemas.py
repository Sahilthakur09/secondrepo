from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime


class UserOut(BaseModel):
    id: int
    linkedin_id: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    headline: Optional[str] = None
    about: Optional[str] = None

    class Config:
        from_attributes = True


class AnalyzeProfileResponse(BaseModel):
    strengths: List[str]
    gaps: List[str]
    brand_voice: str


class TrendItem(BaseModel):
    topic: str
    summary: str


class StrategyRequest(BaseModel):
    industry: Optional[str] = None
    role: Optional[str] = None
    interests: List[str] = Field(default_factory=list)
    frequency_per_week: int = 3


class StrategyItem(BaseModel):
    date: datetime
    post_type: str
    topic: str


class StrategyResponse(BaseModel):
    pillars: List[str]
    calendar: List[StrategyItem]


class GenerateRequest(BaseModel):
    post_type: str
    prompt: str
    language: Optional[str] = "en"


class GenerateResponse(BaseModel):
    content: str
    hashtags: List[str] = Field(default_factory=list)
    metadata: dict = Field(default_factory=dict)


class OptimizeRequest(BaseModel):
    content: str


class OptimizeResponse(BaseModel):
    content: str
    hashtags: List[str]
    suggestions: List[str]


class ScheduleRequest(BaseModel):
    content: str
    post_type: str
    scheduled_at: datetime


class CalendarItem(BaseModel):
    id: int
    content: str
    post_type: str
    status: str
    scheduled_at: Optional[datetime] = None


class SummaryAnalytics(BaseModel):
    total_posts: int
    total_impressions: int
    total_likes: int
    total_comments: int
    total_shares: int


class PostAnalytics(BaseModel):
    post_id: int
    impressions: int
    likes: int
    comments: int
    shares: int
    created_at: datetime


class ABTestRequest(BaseModel):
    variant_a: str
    variant_b: str


class ABTestResponse(BaseModel):
    test_id: str
    status: str