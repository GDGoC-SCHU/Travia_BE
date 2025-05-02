# app/api/v1/endpoints/recommendation.py

from fastapi import APIRouter
from pydantic import BaseModel
from gemini_api.gemini_api_client import generate_travel_recommendation
from app.services.prompt_builder import generate_prompt_from_survey
from app.schemas.survey import SurveyCreate

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/recommend", summary="프롬프트 기반 AI 여행 추천")
def recommend(prompt_req: PromptRequest):
    result = generate_travel_recommendation(prompt_req.prompt)
    if result["status"] == "error":
        return {"error": result["message"]}
    return result

@router.post("/recommend/by-survey", summary="설문 기반 AI 여행 추천")
def recommend_by_survey(survey: SurveyCreate):
    prompt = generate_prompt_from_survey(survey.preferences)
    result = generate_travel_recommendation(prompt)
    if result["status"] == "error":
        return {"error": result["message"]}
    return result
