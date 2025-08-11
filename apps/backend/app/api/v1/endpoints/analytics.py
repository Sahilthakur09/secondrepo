from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class PostMetric(BaseModel):
    post_id: str
    likes: int
    comments: int
    shares: int
    impressions: int
    engagement_rate: float


@router.get("/posts", response_model=List[PostMetric])
async def get_post_metrics() -> List[PostMetric]:
    return [
        PostMetric(
            post_id="abc123",
            likes=120,
            comments=34,
            shares=10,
            impressions=5000,
            engagement_rate=0.032,
        )
    ]