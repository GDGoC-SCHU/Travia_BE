# app/services/prompt_builder.py
# 설문 → Gemini 프롬프트 생성 함수

def generate_prompt_from_survey(preferences) -> str:
    return f"""
다음은 한 여행자의 성향 정보입니다:

- 동행: {preferences.companion}
- 여행 스타일: {preferences.style}
- 여행 기간: {preferences.duration}
- 운전 여부: {preferences.driving}
- 예산: {preferences.budget}
- 선호 기후: {preferences.climate}
- 대륙 선호: {preferences.continent}
- 하루 활동 밀도: {preferences.density}

이 사용자의 성향에 맞는 세계 여행 도시 2~3곳을 추천해 주세요.
추천할만한 도시가 충분하다면 3곳 모두 추천해 주세요.

반드시 아래와 같은 JSON 형식으로 응답해 주세요.
JSON 구조는 정확히 지켜 주세요.  
쉼표 누락이나 중복된 key 없이, 유효한 JSON이 되도록 정확하게 작성해 주세요.
코드블록( ```json )은 제거하고, 순수 JSON만 반환해 주세요.

{{
  "data": [
    {{
      "city": "도시 이름",
      "country": "국가",
      "reason": "성향과의 매칭 이유",
      "schedule": {{
        "day_1": [
          {{ "time": "10:00-13:00", "activity": "활동 설명" }},
          {{ "time": "14:00-17:00", "activity": "활동 설명" }},
          {{ "time": "18:00-20:00", "activity": "활동 설명" }}
        ],
        "day_2": [ ... ],
        "day_3": [ ... ],
        "day_4": [ ... ],
        "day_5": [ ... ]
      }}
    }}
  ]
}}
"""
