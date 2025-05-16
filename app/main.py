from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import survey, auth  
from app.db.init_db import init_db

app = FastAPI(title="Travia API", version="1.0")
init_db()

#  CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(survey.router, prefix="/api/v1/survey") 
app.include_router(auth.router, prefix="/api/auth")         
