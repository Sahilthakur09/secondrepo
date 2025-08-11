from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class ProfileInput(BaseModel):
    headline: str
    summary: str
    experience: List[str]
    skills: List[str]
    interests: List[str] = []


class ProfileInsights(BaseModel):
    strengths: List[str]
    brand_voice: str
    content_pillars: List[str]


@router.post("/analyze", response_model=ProfileInsights)
async def analyze_profile(profile: ProfileInput) -> ProfileInsights:
    strengths = [f"Strong in {skill}" for skill in profile.skills[:5]]
    brand_voice = "Professional, insightful, and action-oriented"
    pillars = ["Industry Trends", "Personal Experiences", "How-To Guides", "Leadership"]
    return ProfileInsights(strengths=strengths, brand_voice=brand_voice, content_pillars=pillars)