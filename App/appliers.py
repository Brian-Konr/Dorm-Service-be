from sqlalchemy.sql.expression import false
from sqlalchemy.sql.operators import exists
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel #used for producing schemas
import models
from database import SessionLocal
from datetime import datetime

db = SessionLocal()

router = APIRouter(
    prefix="/appliers",
    tags=["appliers"],
)


@router.get("/asked/{request_id}")
async def get_all_appliers_for_this_request(request_id: int):
    appliers = db.query(models.Applier).filter(models.Applier.request_id == request_id).all()
    appliers_id = (o.applier_id for o in appliers)
    return db.query(models.User).filter(models.User.user_id.in_(appliers_id)).all()


class Apply(BaseModel): #serializer
    applierId: int
    requestId: int

    class Config:
        orm_mode= True

@router.post('/apply/', status_code= status.HTTP_201_CREATED)
async def make_a_application(item: Apply):

    new_applier = models.Applier(  
        applier_id = item.applierId,
        request_id = item.requestId,
        status = 0
    )
    db_apply_exist = db.query(models.Applier).filter(new_applier.applier_id == models.Applier.applier_id, new_applier.request_id == models.Applier.request_id).first()
    if db_apply_exist is not None:
        raise HTTPException(status_code=404, detail="Apply already exists")
    db.add(new_applier)
    db.commit()

    return