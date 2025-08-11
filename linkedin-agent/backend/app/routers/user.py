from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import UserOut

router = APIRouter(prefix="/api/user", tags=["user"]) 


@router.get("/me", response_model=UserOut)
async def me(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        user = User(full_name="Demo User", headline="Product + AI", about="Demo profile")
        db.add(user)
        db.commit()
        db.refresh(user)
    return user