# 설문 저장 로직

from sqlalchemy.orm import Session
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate

def create_survey(db: Session, survey: SurveyCreate):
    db_survey = Survey(
        username=survey.username,
        preferences=survey.preferences.dict()
    )
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey
