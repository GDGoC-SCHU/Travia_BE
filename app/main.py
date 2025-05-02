from fastapi import FastAPI
from app.api.v1.endpoints import survey, recommendation
from app.db.init_db import init_db

app = FastAPI(title="Travia API", version="1.0")
init_db()

# 라우터 연결
app.include_router(survey.router, prefix="/api/v1")
app.include_router(recommendation.router, prefix="/api/v1")
