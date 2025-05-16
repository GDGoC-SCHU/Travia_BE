from app.models.recommendation import Recommendation
from app.models.survey import Survey
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.survey import SurveyCreate
from app.crud import survey_crud, recommendation_crud
from app.db.session import get_db
from app.services.prompt_builder import generate_prompt_from_survey
from gemini_api.gemini_api_client import generate_travel_recommendation

router = APIRouter()

@router.post("/recommend", summary="Complete the survey and return the AI recommendation results")
def survey_and_recommend(survey: SurveyCreate, db: Session = Depends(get_db)):
    saved_survey = survey_crud.create_survey(db=db, survey=survey)

    prompt = generate_prompt_from_survey(survey.preferences)

    result = generate_travel_recommendation(prompt)

    if result["status"] == "error":
        return {
            "status": "error",
            "message": result["message"]
        }

    saved_rec = recommendation_crud.save_recommendation(
        db=db,
        survey_id=saved_survey.id,  # type: ignore
        result=result["data"]
    )

    return {
        "status": "success",
        "survey_id": saved_survey.id,
        "recommendation_id": saved_rec.id,
        "data": result["data"]
    }

@router.get("/history/{username}", summary="User's Survey + Referral ID Inquiry")
def get_user_recommendation_ids(username: str, db: Session = Depends(get_db)):
    surveys = db.query(Survey).filter(Survey.username == username).all()
    results = []

    for s in surveys:
        rec = db.query(Recommendation).filter(Recommendation.survey_id == s.id).first()
        if rec:
            results.append({
                "survey_id": s.id,
                "recommendation_id": rec.id
            })

    return {"status": "success", "results": results}


@router.get("/detail/{survey_id}", summary="Get survey + recommendation details by ID")
def get_survey_detail(survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    recommendation = db.query(Recommendation).filter(Recommendation.survey_id == survey_id).first()

    return {
        "status": "success",
        "survey_id": survey.id,
        "username": survey.username,
        "preferences": survey.preferences,
        "recommendation": recommendation.result if recommendation else None
    }


@router.delete("/delete/{survey_id}", summary="Delete a survey and its recommendation")
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    rec = db.query(Recommendation).filter(Recommendation.survey_id == survey_id).first()
    if rec:
        db.delete(rec)

    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    db.delete(survey)

    db.commit()
    return {"status": "success", "message": "Survey and recommendation deleted"}





