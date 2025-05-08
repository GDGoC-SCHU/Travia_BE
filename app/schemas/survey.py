# app/schemas/survey.py
# Pydantic 요청 스키마

from pydantic import BaseModel

class Preferences(BaseModel):
    companion: str
    style: str
    duration: str
    driving: str
    budget: str
    climate: str
    continent: str
    density: str

class SurveyCreate(BaseModel):
    username: str
    preferences: Preferences

