from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    id = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
