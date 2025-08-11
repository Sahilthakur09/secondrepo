from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime

from ..database import get_db
from ..models import User, OAuthToken
from ..services import linkedin

router = APIRouter(prefix="/api/auth/linkedin", tags=["auth"]) 


@router.get("/login")
async def login():
    state = str(uuid4())
    url = linkedin.get_auth_url(state)
    return {"redirect": url}


@router.get("/callback")
async def callback(code: str | None = None, state: str | None = None, db: Session = Depends(get_db)):
    if code is None:
        raise HTTPException(status_code=400, detail="Missing code")
    token = linkedin.exchange_code_for_token(code)

    # In demo, create or get a single user
    profile = linkedin.get_profile(token["access_token"])  # type: ignore[index]
    linkedin_id = profile.get("id")
    user = db.query(User).filter(User.linkedin_id == linkedin_id).first()
    if not user:
        user = User(
            linkedin_id=linkedin_id,
            full_name=f"{profile.get('localizedFirstName')} {profile.get('localizedLastName')}",
            headline=profile.get("headline"),
            about=profile.get("summary"),
            email=profile.get("email"),
        )
        db.add(user)
        db.flush()

    tokens = db.query(OAuthToken).filter(OAuthToken.user_id == user.id).first()
    if not tokens:
        tokens = OAuthToken(user_id=user.id)
        db.add(tokens)
    tokens.access_token = token.get("access_token")  # type: ignore[arg-type]
    tokens.refresh_token = token.get("refresh_token")  # type: ignore[arg-type]
    tokens.expires_at = token.get("expires_at")  # type: ignore[arg-type]

    db.commit()

    return {"status": "connected", "user_id": user.id}