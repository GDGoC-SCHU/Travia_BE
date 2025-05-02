# 추천 결과 저장 로직

from sqlalchemy.orm import Session
from app.models.recommendation import Recommendation

def save_recommendation(db: Session, survey_id: int, result: dict):
    rec = Recommendation(survey_id=survey_id, result=result)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec
