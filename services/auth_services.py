from sqlalchemy.orm import Session
from models.users import Users
from schemas.auth_schemas import RegisterUser, LoginUser
from sqlalchemy import select
from core.security import hash_password, verify_password, create_token



def register(db: Session, user: RegisterUser):
    check_admin = db.execute(select(Users)).first()
    if not check_admin:
        role = "ADMIN"
    role = "USER"
    check_user = db.execute(select(Users).where(Users.email == user.email)).first()
    if check_user:
        return None
    db.add(Users(email = user.email, hashed_password = hash_password(user.password), role = role))
    db.commit()
    return True

def login(db: Session, user_data: LoginUser):
    get_user = db.execute(select(Users).where(Users.email == user_data.email)).first()
    if not get_user:
        return None
    if verify_password(user_data.password, get_user.hashed_password):
        return create_token({"sub": get_user.user_id})
    return None