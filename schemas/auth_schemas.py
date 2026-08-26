from pydantic import BaseModel, EmailStr, field_validator
import re

class RegisterUser(BaseModel):
    email: EmailStr
    password: str
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("password must be at least 8 characters")
        if not re.search(r'[0-9]', v):
            raise ValueError("password must have a number")
        if not re.search(r'[@$!%*?&._-]', v):
            raise ValueError("password must have a special character")
        return v

class LoginUser(BaseModel):
    email: EmailStr
    password: str
    