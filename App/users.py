from fastapi import APIRouter, status, HTTPException
import models
from database import SessionLocal
from schemas import User as UserSchema

db = SessionLocal()

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def read_users():
    return db.query(models.User).all()

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
        return "user created successfully"



