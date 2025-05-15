# Pydantic 요청 스키마

from pydantic import BaseModel
from typing import List

class Preferences(BaseModel):
    companion: str
    style: List[str]
    duration: str
    driving: str
    budget: str
    climate: str
    continent: str
    density: str

class SurveyCreate(BaseModel):
    username: str
    preferences: Preferences

