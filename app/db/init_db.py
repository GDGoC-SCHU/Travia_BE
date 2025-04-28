# app/db/init_db.py (새로 만들 파일)

from app.db.session import engine
from app.models import survey
from app.db.base import Base

def init_db():
    Base.metadata.create_all(bind=engine)
