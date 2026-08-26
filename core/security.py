from passlib.context import CryptContext
from jose import jwt
from core.settings import settings
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer

oauth = OAuth2PasswordBearer(tokenUrl="auth/login")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain_password: str):
    return password_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str):
    return password_context.verify(plain_password, hashed_password)

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.token_duration)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
