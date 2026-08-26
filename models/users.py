from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, Enum
import uuid
from typing import Literal

class Users(Base):
    __tablename__ = "users"
    user_id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    role: Mapped[Literal["ADMIN", "USER"]] = mapped_column(Enum("ADMIN", "USER", name="user_roles"))
    created_at: Mapped[str] = mapped_column(server_default=func.now())