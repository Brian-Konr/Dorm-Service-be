from sqlalchemy.sql.expression import false
from sqlalchemy.sql.operators import exists
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel #used for producing schemas
import models
from database import SessionLocal
from datetime import datetime



db = SessionLocal()

router = APIRouter(
    prefix="/locations",
    tags=["locations"],
)

@router.get("/")
async def get_all_locations_info():
    return db.query(models.Location).all()

@router.get("/{classId}")
async def get_specific_classId_location(classId: int):
    q = db.query(models.LocationClas).filter(models.LocationClas.class_id == classId)
    if q.count():
        return db.query(models.Location).filter(models.Location._class == classId).all()
    else:
        raise HTTPException(status_code=404, detail="Class id not found in User list")

