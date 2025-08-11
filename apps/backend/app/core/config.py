from functools import lru_cache
from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import List
import os


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "development")
    secret_key: str = os.getenv("SECRET_KEY", "change-me")

    # CORS
    cors_allow_origins: List[AnyHttpUrl] = []  # can be set via env later

    # Database
    postgres_user: str = os.getenv("POSTGRES_USER", "influenceos")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "influenceos")
    postgres_db: str = os.getenv("POSTGRES_DB", "influenceos")
    postgres_host: str = os.getenv("POSTGRES_HOST", "db")
    postgres_port: str = os.getenv("POSTGRES_PORT", "5432")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    # Redis
    redis_url: str = os.getenv("REDIS_URL", "redis://redis:6379/0")

    # OAuth (LinkedIn)
    linkedin_client_id: str = os.getenv("LINKEDIN_CLIENT_ID", "")
    linkedin_client_secret: str = os.getenv("LINKEDIN_CLIENT_SECRET", "")
    linkedin_redirect_uri: str = os.getenv("LINKEDIN_REDIRECT_URI", "http://localhost:3000/oauth/linkedin/callback")

    # AI providers
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    default_model: str = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")

    @validator("cors_allow_origins", pre=True)
    def parse_cors_origins(cls, v):
        env_val = os.getenv("CORS_ALLOW_ORIGINS")
        if env_val:
            return [o.strip() for o in env_val.split(",") if o.strip()]
        return v


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()