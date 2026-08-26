from dependencies.auth import decode_jwt
from models.users import Users
from fastapi import Depends, HTTPException


def verify_admin(user: Users = Depends(decode_jwt)):
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="You're Not Allowed")
    return user