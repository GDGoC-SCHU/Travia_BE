# DB 테이블 생성

from app.db.session import engine
from app.models import survey, recommendation  # ✅ recommendation 꼭 포함
from app.db.base import Base

def init_db():
    Base.metadata.create_all(bind=engine)
