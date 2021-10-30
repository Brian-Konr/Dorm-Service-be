from fastapi import APIRouter
import models
from database import SessionLocal

db = SessionLocal()

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return db.query(models.User).all()
