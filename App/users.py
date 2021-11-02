from fastapi import APIRouter, status, HTTPException
import models
from database import SessionLocal
from pydantic import BaseModel
from schemas import User as UserSchema

db = SessionLocal()

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

class Login(BaseModel): #serializer
    userName: str
    password: str
    class Config:
        orm_mode= True

@router.get('/') 
async def get_all_users():
    return db.query(models.User).all()

@router.get("/{user_id}")
async def get_specific_user(user_id: int):
    q = db.query(models.User).filter(models.User.user_id == user_id)
    if q.count():
        return db.query(models.User).filter(models.User.user_id == user_id).first()
    else:
        raise HTTPException(status_code=404, detail="User id not found in User list")

@router.post("/login") #The reason I use post is because get cannot have a request body, and I didn't know how to handle this situation.
async def test_login(login: Login):
    q = db.query(models.User).filter(models.User.user_name == login.userName, models.User.password == login.password)
    if q.count():
        user = db.query(models.User).filter(models.User.user_name == login.userName, models.User.password == login.password).first()
        return user.user_id
    else:
        raise HTTPException(status_code=404, detail="The combination of username and password not found in User list")


@router.post("/", status_code= status.HTTP_201_CREATED)
async def create_new_user(user: UserSchema):
    newUser = models.User(
        user_name = user.userName,
        gender = user.gender,
        phone_num = user.phoneNum,
        fb_url = user.fbUrl,
        dorm_id = user.dormID,
        password = user.password
    )
    db_name_exist = db.query(models.User).filter(newUser.user_name == models.User.user_name).first()
    if db_name_exist is not None:
        raise HTTPException(status_code=400, detail="User name already exists")
    else:
        db.add(newUser)
        db.commit()
        serviceId = 1
        while(serviceId < 5):
            newUserInputEntry = models.UserPoint(
                user_id = newUser.user_id,
                service_id = serviceId,
            )
            db.add(newUserInputEntry)
            db.commit()
            serviceId += 1

        return newUser.user_id




