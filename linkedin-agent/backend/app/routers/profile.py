from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import AnalyzeProfileResponse
from ..services.llm import analyze_profile_text

router = APIRouter(prefix="/api/profile", tags=["profile"]) 


@router.post("/analyze", response_model=AnalyzeProfileResponse)
async def analyze(db: Session = Depends(get_db)):
    user = db.query(User).first()
    profile_text = (user.about or "") + "\n" + (user.headline or "")
    strengths, gaps, voice = analyze_profile_text(profile_text)
    return AnalyzeProfileResponse(strengths=strengths, gaps=gaps, brand_voice=voice)