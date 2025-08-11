from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "LinkedIn Personal Branding AI Agent"
    app_base_url: str = Field(default="http://localhost:8000", alias="APP_BASE_URL")

    database_url: str = Field(default="sqlite:///./app.db", alias="DATABASE_URL")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")

    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")

    linkedin_client_id: str | None = Field(default=None, alias="LINKEDIN_CLIENT_ID")
    linkedin_client_secret: str | None = Field(default=None, alias="LINKEDIN_CLIENT_SECRET")
    linkedin_redirect_uri: str | None = Field(default=None, alias="LINKEDIN_REDIRECT_URI")

    secret_key: str = Field(default="change_me", alias="SECRET_KEY")
    token_algorithm: str = Field(default="HS256", alias="TOKEN_ALGORITHM")
    token_expire_minutes: int = Field(default=60, alias="TOKEN_EXPIRE_MINUTES")

    demo_mode: bool = Field(default=True, alias="DEMO_MODE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        populate_by_name = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore[arg-type]