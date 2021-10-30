from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel #used for producing schemas
import models
from database import SessionLocal
from datetime import datetime



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


class Drive(BaseModel): #serializer 從前端接收???
    requesterId:     int
    title:           str
    endTime:         str
    actStartTime:    str
    actEndTime:      str
    reward:          str
    description:     str
    fromId:          int
    toId:            int

    class Config:
        orm_mode= True

@router.post('/drive', status_code= status.HTTP_201_CREATED)
async def create_drive(drive: Drive): #接到 名稱: 型別
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_re = models.Request(  
        requester_id = drive.requesterId,
        service_id = 1,
        description = drive.description,
        start_time = now,
        end_time = drive.endTime,
        act_start_time = drive.actStartTime,
        act_end_time = drive.actEndTime,
        reward = drive.reward,
        title = drive.title
    )
    db.add(new_re)
    db.commit()

    new_drive = models.DriveServicePost(
        request_id = new_re.request_id,
        from_id = drive.fromId,
        to_id = drive.toId
    )

    db.add(new_drive)
    db.commit()

    return new_re.request_id
