from fastapi import APIRouter
from ..schemas import TrendItem
from ..services.llm import generate_trends

router = APIRouter(prefix="/api/trends", tags=["trends"]) 


@router.get("", response_model=list[TrendItem])
async def list_trends(industry: str | None = None):
    items = generate_trends(industry)
    return [TrendItem(**i) for i in items]