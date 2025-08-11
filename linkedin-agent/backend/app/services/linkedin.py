from __future__ import annotations
from typing import Optional, Tuple, Dict, Any
from urllib.parse import urlencode
from datetime import datetime, timedelta
import uuid

from ..config import get_settings

settings = get_settings()


def get_auth_url(state: str) -> str:
    if settings.demo_mode:
        return f"/api/auth/linkedin/callback?code=demo-code&state={state}"
    params = {
        "response_type": "code",
        "client_id": settings.linkedin_client_id,
        "redirect_uri": settings.linkedin_redirect_uri,
        "scope": "r_liteprofile r_emailaddress w_member_social",
        "state": state,
    }
    return "https://www.linkedin.com/oauth/v2/authorization?" + urlencode(params)


def exchange_code_for_token(code: str) -> Dict[str, Any]:
    if settings.demo_mode:
        return {
            "access_token": "demo-access-token",
            "refresh_token": "demo-refresh-token",
            "expires_at": datetime.utcnow() + timedelta(hours=2),
        }
    # In production, exchange via LinkedIn token endpoint
    raise NotImplementedError("Real LinkedIn token exchange not implemented in scaffold.")


def get_profile(access_token: str) -> Dict[str, Any]:
    if settings.demo_mode:
        return {
            "id": "demo-linkedin-id",
            "localizedFirstName": "Demo",
            "localizedLastName": "User",
            "headline": "Product Manager | Building with AI",
            "summary": "I build delightful products at the intersection of UX and AI.",
            "email": "demo@example.com",
        }
    raise NotImplementedError


def create_post(access_token: str, content: str, post_type: str) -> Tuple[str, datetime]:
    if settings.demo_mode:
        return str(uuid.uuid4()), datetime.utcnow()
    raise NotImplementedError


def fetch_post_metrics(access_token: str, platform_post_id: str) -> Dict[str, int]:
    if settings.demo_mode:
        import random
        return {
            "impressions": random.randint(100, 5000),
            "likes": random.randint(1, 300),
            "comments": random.randint(0, 50),
            "shares": random.randint(0, 25),
        }
    raise NotImplementedError