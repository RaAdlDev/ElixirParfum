from jose import jwt, JWTError
from core.settings import settings
from core.security import oauth
from fastapi import Depends, HTTPException
from database.connection import get_db
from models.users import Users
from sqlalchemy.orm import Session

def decode_jwt(token: str = Depends(oauth), db: Session = Depends(get_db)):
    try:
        decoded_payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id = decoded_payload['sub']
        if not user_id :
            raise HTTPException(status_code=401, detail="User Not Found")
        user = db.get(Users, user_id)
        if not user:
            raise HTTPException(status_code=401, detail="User Not Found")
        if user.is_active == False:
            raise HTTPException(status_code=409, detail="Inactive User")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="You're Not Allowed")
