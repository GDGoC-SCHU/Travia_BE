# DB 연결

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# ✅ 환경변수 우선순위: SQLALCHEMY_DATABASE_URL > DATABASE_URL
SQLALCHEMY_DATABASE_URL = (
    os.getenv("SQLALCHEMY_DATABASE_URL")
    or os.getenv("DATABASE_URL")
)

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("❌ DB 연결 문자열이 환경변수에 없습니다 (.env에 SQLALCHEMY_DATABASE_URL 또는 DATABASE_URL 필요)")

# ✅ DB 연결 및 세션 설정
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ FastAPI 의존성 주입용
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
