import requests
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.operators import exists
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
    return db.query(models.Request).all()

class Drive(BaseModel): #serializer
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
async def create_drive(item: Drive): #接到 名稱: 型別
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_re = models.Request(  
        requester_id = item.requesterId,
        service_id = 1,
        description = item.description,
        start_time = now,
        end_time = item.endTime,
        act_start_time = item.actStartTime,
        act_end_time = item.actEndTime,
        reward = item.reward,
        title = item.title
    )

    db.add(new_re)
    db.commit()

    new_drive = models.DriveServicePost(
        # request_id = new_re.request_id,
        from_id = item.fromId,
        to_id = item.toId,
        re = new_re
    )

    db.add(new_drive)
    db.commit()

    return new_re.request_id


class Heavy(BaseModel): #serializer
    requesterId:     int
    title:           str
    endTime:         str
    actStartTime:    str
    actEndTime:      str
    reward:          str
    description:     str
    fromId:          int
    fromFloor:       int
    toId:            int
    toFloor:         int
    item:            str
    itemWeight:      str

    class Config:
        orm_mode= True

@router.post('/heavyLifting', status_code= status.HTTP_201_CREATED)
async def create_heavyLifting(item: Heavy): #接到 名稱: 型別
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_re = models.Request(  
        requester_id = item.requesterId,
        service_id = 2,
        description = item.description,
        start_time = now,
        end_time = item.endTime,
        act_start_time = item.actStartTime,
        act_end_time = item.actEndTime,
        reward = item.reward,
        title = item.title
    )

    db.add(new_re)
    db.commit()

    new_heavy = models.HeavyliftingServicePost(
        from_id = item.fromId,
        from_floor = item.fromFloor,
        to_id = item.toId,
        to_floor = item.toFloor,
        item = item.item,
        item_weight = item.itemWeight,
        re = new_re
    )

    db.add(new_heavy)
    db.commit()

    return new_re.request_id

class Kill(BaseModel): #serializer
    requesterId:     int
    title:           str
    endTime:         str
    actStartTime:    str
    actEndTime:      str
    reward:          str
    description:     str
    requesterLocationId: int

    class Config:
        orm_mode= True

@router.post('/kill', status_code= status.HTTP_201_CREATED)
async def create_kill_cockroach(item: Kill): #接到 名稱: 型別
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_re = models.Request(  
        requester_id = item.requesterId,
        service_id = 3,
        description = item.description,
        start_time = now,
        end_time = item.endTime,
        act_start_time = item.actStartTime,
        act_end_time = item.actEndTime,
        reward = item.reward,
        title = item.title
    )

    db.add(new_re)
    db.commit()

    new_kill = models.KillCockroachServicePost(
        requester_location_id = item.requesterLocationId,
        re = new_re
    )

    db.add(new_kill)
    db.commit()

    return new_re.request_id



class Event(BaseModel): #serializer
    requesterId:     int
    title:           str
    endTime:         str
    actStartTime:    str
    actEndTime:      str
    description:     str
    eventLocationId: int
    locationDetail:  str

    class Config:
        orm_mode= True

@router.post('/hostEvent', status_code= status.HTTP_201_CREATED)
async def create_event(item: Event): #接到 名稱: 型別
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_re = models.Request(  
        requester_id = item.requesterId,
        service_id = 4,
        description = item.description,
        start_time = now,
        end_time = item.endTime,
        act_start_time = item.actStartTime,
        act_end_time = item.actEndTime,
        title = item.title
    )

    db.add(new_re)
    db.commit()

    new_event = models.HostEventPost(
        event_location_id = item.eventLocationId,
        location_detail = item.locationDetail,
        re = new_re
    )

    db.add(new_event)
    db.commit()

    return new_re.request_id

# @router.get("/{request_id}")
# async def get_a_request(request_id: int):
#     return db.query(models.Request).filter(models.Request.request_id == request_id).all()

@router.get("/drive/{request_id}")
async def get_a_drive_request(request_id: int):
    q = db.query(models.DriveServicePost).filter(models.DriveServicePost.request_id == request_id)
    if q.count():
        return db.query(models.DriveServicePost, models.Request).filter(models.Request.request_id == request_id, models.DriveServicePost.request_id == request_id).all()
    else:
        raise HTTPException(status_code=404, detail="Request id not found in Drive Service Post")
    

@router.get("/heavyLifting/{request_id}")
async def get_a_heavyLifting_request(request_id: int):
    q = db.query(models.HeavyliftingServicePost).filter(models.HeavyliftingServicePost.request_id == request_id)
    if q.count():
        return db.query(models.HeavyliftingServicePost, models.Request).filter(models.Request.request_id == request_id, models.HeavyliftingServicePost.request_id == request_id).all()
    else:
        raise HTTPException(status_code=404, detail="Request id not found in Heavy lifting Service Post")

@router.get("/kill/{request_id}")
async def get_a_kill_request(request_id: int):
    q = db.query(models.KillCockroachServicePost).filter(models.KillCockroachServicePost.request_id == request_id)
    if q.count():
        return db.query(models.KillCockroachServicePost, models.Request).filter(models.Request.request_id == request_id, models.KillCockroachServicePost.request_id == request_id).all()
    else:
        raise HTTPException(status_code=404, detail="Request id not found in Kill Cockroach Service Post")

@router.get("/hostEvent/{request_id}")
async def get_a_hostEvent_request(request_id: int):
    q = db.query(models.HostEventPost).filter(models.HostEventPost.request_id == request_id)
    if q.count():
        return db.query(models.HostEventPost, models.Request).filter(models.Request.request_id == request_id, models.HostEventPost.request_id == request_id).all()
    else:
        raise HTTPException(status_code=404, detail="Request id not found in Host Event Post")

@router.get("/available")
async def get_all_available_requests():
    return db.query(models.Request).filter(models.Request.end_time >= datetime.now()).all()

@router.get("/{applier_id}")
async def get_all_requests_and_status_for_this_applier(applier_id: int):
    return db.query(models.Applier.status, models.Request).filter(models.Applier.applier_id == applier_id).all()


class Request_Applier(BaseModel): #serializer
    requestId:      int
    applierId:      int

    class Config:
        orm_mode= True

@router.patch("/accept", status_code = status.HTTP_200_OK)
async def accept_request(item: Request_Applier):
    requestId = item.requestId
    applierId = item.applierId

    item_to_update = db.query(models.Applier).filter(models.Applier.request_id == requestId, models.Applier.applier_id == applierId)

    if item_to_update.count():
        item_to_update.first().status = 1
        db.add(item_to_update.first())
        db.commit()

        updated_item = db.query(models.Applier).filter(models.Applier.request_id == requestId, models.Applier.applier_id == applierId).first()
        return updated_item
    
    else:
        raise HTTPException(status_code=404, detail="Application data not in Appliers table")

@router.patch("/refuse", status_code = status.HTTP_200_OK)
async def refuse_request(item: Request_Applier):
    requestId = item.requestId
    applierId = item.applierId

    item_to_update = db.query(models.Applier).filter(models.Applier.request_id == requestId, models.Applier.applier_id == applierId)

    if item_to_update.count():
        item_to_update.first().status = 2
        db.add(item_to_update.first())
        db.commit()

        updated_item = db.query(models.Applier).filter(models.Applier.request_id == requestId, models.Applier.applier_id == applierId).first()
        return updated_item
    
    else:
        raise HTTPException(status_code=404, detail="Application data not in Appliers table")
