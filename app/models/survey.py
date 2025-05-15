# 설문 테이블 모델

from sqlalchemy import Column, Integer, String, JSON, TIMESTAMP, func
from app.db.base import Base

class Survey(Base):
    __tablename__ = "survey"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    preferences = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
