from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.survey import SurveyCreate
from app.crud import survey_crud, recommendation_crud
from app.db.session import get_db
from app.services.prompt_builder import generate_prompt_from_survey
from gemini_api.gemini_api_client import generate_travel_recommendation

router = APIRouter()

@router.post("/recommend", summary="설문 작성 및 AI 추천 결과 반환")
def survey_and_recommend(survey: SurveyCreate, db: Session = Depends(get_db)):
    # 1. 설문 저장
    saved_survey = survey_crud.create_survey(db=db, survey=survey)

    # 2. 프롬프트 생성
    prompt = generate_prompt_from_survey(survey.preferences)

    # 3. Gemini 호출
    result = generate_travel_recommendation(prompt)

    if result["status"] == "error":
        return {
            "status": "error",
            "message": result["message"]
        }

    # 4. 추천 결과 저장
    saved_rec = recommendation_crud.save_recommendation(
        db=db,
        survey_id=saved_survey.id,  # type: ignore
        result=result["data"]
    )

    # 5. 최종 응답
    return {
        "status": "success",
        "survey_id": saved_survey.id,
        "recommendation_id": saved_rec.id,
        "data": result["data"]
    }

@router.get("/ping")
async def ping():
    return {"message": "pong"}
