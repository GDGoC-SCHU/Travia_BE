# app/schemas/survey.py

from pydantic import BaseModel
from typing import Dict

class SurveyCreate(BaseModel):
    username: str
    preferences: Dict[str, str]  # 설문 결과 (질문-답변 형태)
