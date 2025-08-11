from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class ResearchRequest(BaseModel):
    industry: str
    role: str | None = None
    language: str = "en"


class ResearchItem(BaseModel):
    topic: str
    summary: str
    sources: List[str]


@router.post("/trends", response_model=List[ResearchItem])
async def research_trends(req: ResearchRequest) -> List[ResearchItem]:
    items = [
        ResearchItem(
            topic=f"GenAI adoption in {req.industry}",
            summary="How companies are moving from pilots to production with governance and ROI focus",
            sources=["https://example.com/industry-report", "https://news.example.com/article"],
        ),
        ResearchItem(
            topic="Data privacy regulations",
            summary="Emerging compliance requirements affecting go-to-market and product roadmaps",
            sources=["https://example.com/privacy-update"],
        ),
    ]
    return items