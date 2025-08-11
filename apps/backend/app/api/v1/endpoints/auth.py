from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ....core.config import settings

router = APIRouter()


class OAuthUrlResponse(BaseModel):
    authorization_url: str


@router.get("/linkedin/login", response_model=OAuthUrlResponse)
async def linkedin_login() -> OAuthUrlResponse:
    base = "https://www.linkedin.com/oauth/v2/authorization"
    params = (
        f"response_type=code&client_id={settings.linkedin_client_id}"
        f"&redirect_uri={settings.linkedin_redirect_uri}&scope=r_liteprofile%20r_emailaddress%20w_member_social"
        f"&state=secure_random_state"
    )
    return OAuthUrlResponse(authorization_url=f"{base}?{params}")


class TokenExchangeRequest(BaseModel):
    code: str
    state: str


class TokenExchangeResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    expires_in: int | None = None


@router.post("/linkedin/callback", response_model=TokenExchangeResponse)
async def linkedin_callback(payload: TokenExchangeRequest) -> TokenExchangeResponse:
    # TODO: exchange code for token via LinkedIn API; for now, mock
    if not payload.code:
        raise HTTPException(status_code=400, detail="Missing authorization code")
    return TokenExchangeResponse(access_token="mock_access_token", expires_in=3600)