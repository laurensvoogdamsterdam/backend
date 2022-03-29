from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from backend.db import db_user
from backend.db.database import get_db
from backend.routers.schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
