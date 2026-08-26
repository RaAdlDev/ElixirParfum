from fastapi import APIRouter, Depends, HTTPException
from services.auth_services import register, login
from database.connection import get_db
from sqlalchemy.orm import Session
from schemas.auth_schemas import RegisterUser, LoginUser

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
async def register_user(user_data: RegisterUser, db: Session =  Depends(get_db)):
    status = register(db, user_data)
    if status:
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(status_code=409, detail="Try another data")

@router.post("/login")
async def login_user(user_data: LoginUser, db: Session = Depends(get_db)):
    status = login()
    if status is None:
        raise HTTPException(status_code=401, detail="Invalid data")
    return status