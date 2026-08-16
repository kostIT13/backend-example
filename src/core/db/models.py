from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, ForeignKey
from src.core.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)

class Post(Base):
    __tablename__ = "posts"
    
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)