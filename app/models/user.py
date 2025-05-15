from sqlalchemy import Column, Integer, String
from app.db.base import Base

from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    nickname = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)