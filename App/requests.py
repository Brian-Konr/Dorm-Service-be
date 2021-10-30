from fastapi import APIRouter
import models
from database import SessionLocal

db = SessionLocal()

router = APIRouter(
    prefix="/requests",
    tags=["requests"],
)


@router.get("/")
async def get_all_requests():
    return db.query(models.User).all()

@router.get("/re")
async def read_users():
    return db.query(models.User).all()

