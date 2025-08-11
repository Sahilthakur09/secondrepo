from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.routes import api_router
from .core.db import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(
        title="Influence OS - LinkedIn Personal Branding AI",
        version="0.1.0",
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        description="Backend API for autonomous LinkedIn personal branding agent",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create tables (simple auto-migrate for MVP)
    Base.metadata.create_all(bind=engine)

    app.include_router(api_router, prefix="/api")

    return app


app = create_app()