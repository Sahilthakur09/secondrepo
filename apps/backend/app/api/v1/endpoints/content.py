from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Literal
from ....services.ai_orchestrator import AIPipelineOrchestrator
from ....services.compliance import check_and_adjust_content

router = APIRouter()


class GenerateContentRequest(BaseModel):
    industry: str
    role: str
    interests: List[str] = []
    brand_voice: str = "Professional, helpful"
    format: Literal["text", "article", "carousel", "poll"] = "text"
    topic_hint: str | None = None
    language: str = "en"


class GeneratedContent(BaseModel):
    title: str | None = None
    body: str
    hashtags: List[str]
    call_to_action: str | None = None
    compliance_notices: List[str] = []


@router.post("/generate", response_model=GeneratedContent)
async def generate_content(req: GenerateContentRequest) -> GeneratedContent:
    try:
        orchestrator = AIPipelineOrchestrator()
        content = await orchestrator.generate_content(
            industry=req.industry,
            role=req.role,
            interests=req.interests,
            brand_voice=req.brand_voice,
            content_format=req.format,
            topic_hint=req.topic_hint,
            language=req.language,
        )
        adjusted_body, notices = check_and_adjust_content(content["body"])
        content["body"] = adjusted_body
        content["compliance_notices"] = notices
        return GeneratedContent(**content)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


class HashtagRequest(BaseModel):
    topic: str
    industry: str
    max_hashtags: int = 10


class HashtagResponse(BaseModel):
    hashtags: List[str]


@router.post("/hashtags", response_model=HashtagResponse)
async def suggest_hashtags(req: HashtagRequest) -> HashtagResponse:
    base = req.topic.lower().replace(" ", "")
    tags = {f"#{base}", f"#{req.industry.lower()}", "#leadership", "#careerdevelopment", "#productivity"}
    return HashtagResponse(hashtags=list(tags)[: req.max_hashtags])