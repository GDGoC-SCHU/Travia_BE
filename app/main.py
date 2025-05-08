from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import survey
from app.db.init_db import init_db

app = FastAPI(title="Travia API", version="1.0")
init_db()

# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 또는 ["*"]로 임시 전체 허용 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 연결
app.include_router(survey.router, prefix="/api/v1")
