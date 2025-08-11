from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .config import get_settings
from .database import Base, engine
from .routers import auth, user, profile, trends, content, analytics, jobs, health
from .services.scheduler import start_scheduler

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(profile.router)
app.include_router(trends.router)
app.include_router(content.router)
app.include_router(analytics.router)
app.include_router(jobs.router)


@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(bind=engine)
    start_scheduler()