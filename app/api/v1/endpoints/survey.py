# app/api/v1/endpoints/survey.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.survey import SurveyCreate
from app.crud import survey_crud
from app.db.session import get_db

router = APIRouter()

@router.post("/survey", summary="설문 제출")
def create_survey(survey: SurveyCreate, db: Session = Depends(get_db)):
    return survey_crud.create_survey(db=db, survey=survey)

@router.get("/ping")
async def ping():
    return {"message": "pong"}
