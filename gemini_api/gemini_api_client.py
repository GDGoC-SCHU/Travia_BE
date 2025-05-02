# 필요한 라이브러리 불러오기
import os                            # 환경변수 사용을 위한 os 모듈
import json                          # JSON 문자열 → Python dict 변환을 위한 json 모듈
from dotenv import load_dotenv       # .env 파일에서 환경변수를 불러오기 위한 dotenv 모듈
import google.generativeai as genai  # Google Generative AI (Gemini API) 사용을 위한 모듈

# .env 파일에서 GOOGLE_API_KEY 읽어오기
load_dotenv()


# 환경변수에서 API 키 가져오기
api_key = os.getenv("GOOGLE_API_KEY")

# API 키가 설정되지 않은 경우 에러 발생
if not api_key:
    raise ValueError("[ERROR] GOOGLE_API_KEY가 설정되지 않았습니다!")

# Gemini API 설정 (API 키로 인증)
genai.configure(api_key=api_key)

# 사용할 모델 지정 (Gemini 1.5 Flash 최신 버전)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# ---------------------------------------------
# Markdown 코드블록(```json ... ```)을 제거하는 함수
# ---------------------------------------------
def clean_markdown_json(response_text: str) -> str:
    # 응답이 ```json 으로 시작하면 그 부분을 잘라냄
    if response_text.startswith("```json"):
        response_text = response_text[len("```json"):].strip()
    # 응답이 ``` 으로 끝나면 그 부분도 잘라냄
    if response_text.endswith("```"):
        response_text = response_text[:-len("```")].strip()
    # 코드블록 제거된 JSON 문자열 반환
    return response_text

# ---------------------------------------------------
# Gemini API로 여행 추천 결과 생성 및 JSON 반환 함수
# ---------------------------------------------------
def generate_travel_recommendation(prompt: str) -> dict:
    try:
        # 사용자가 입력한 prompt를 기반으로 Gemini API 호출
        response = model.generate_content(prompt)

        # 응답에서 결과 텍스트 추출:
        # 기본적으로 response.parts[0].text에 결과가 들어있음 (없으면 response.text 사용)
        result_text = response.parts[0].text if hasattr(response, "parts") and response.parts else response.text

        # Gemini가 응답한 원본 출력 (디버깅용)
        print("\n[Gemini 원본 응답]\n")
        print(result_text)

        # Markdown 코드블록 제거 (```json ... ```)
        cleaned_text = clean_markdown_json(result_text)

        # JSON 문자열을 Python 딕셔너리로 파싱
        parsed_result = json.loads(cleaned_text)

        # 중첩된 "data": {"data": ...} 구조를 제거하고 깔끔하게 반환
        return {
            "status": "success",             # 성공 상태 반환
            "data": parsed_result["data"],    # 실제 여행 추천 결과 리스트만 반환
        }

    # 예외 처리: 파싱 실패나 API 호출 문제 시 에러 메시지 반환
    except Exception as e:
        print(f"[ERROR] Gemini API 호출 중 오류 발생: {e}")
        return {
            "status": "error",               # 실패 시 에러 상태
            "message": str(e)                # 오류 메시지 상세 전달
        }
