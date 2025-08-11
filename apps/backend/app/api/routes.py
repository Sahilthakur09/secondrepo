from fastapi import APIRouter
from .v1.endpoints import auth, profile, content, calendar, analytics, schedule, research

api_router = APIRouter()

api_v1 = APIRouter(prefix="/v1")
api_v1.include_router(auth.router, prefix="/auth", tags=["auth"])
api_v1.include_router(profile.router, prefix="/profile", tags=["profile"])
api_v1.include_router(content.router, prefix="/content", tags=["content"])
api_v1.include_router(calendar.router, prefix="/calendar", tags=["calendar"])
api_v1.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
api_v1.include_router(schedule.router, prefix="/schedule", tags=["schedule"])
api_v1.include_router(research.router, prefix="/research", tags=["research"])

api_router.include_router(api_v1)