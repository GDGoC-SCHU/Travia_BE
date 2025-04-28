
# 🌍 Travia Backend

**AI 여행 성향 기반 세계 여행지 + 일정 추천 서비스**  
Travia는 사용자의 간단한 설문 응답을 바탕으로, Google Gemini API를 통해  
성향에 맞는 여행 도시와 일자별 일정을 자동으로 생성해주는 추천 서비스입니다.

---

## ✅ 주요 기능

- 설문 응답을 DB에 저장
- 설문 결과 기반 프롬프트 자동 생성
- Google Gemini 1.5 Flash API 연동
- 도시 추천 + 4박 5일 일정표 생성
- 추천 결과를 DB에 저장 및 응답

---

## 🧱 현재 프로젝트 구조

```
trivia/
├── .env                        # 환경 변수 설정 파일
├── gemini_api/
│   └── gemini_api_client.py    # Gemini API 호출 및 JSON 파싱
├── app/
│   ├── main.py                 # FastAPI 앱 정의 및 라우터 등록
│   ├── api/v1/endpoints/
│   │   └── survey.py           # 설문 + 추천 API 정의
│   ├── crud/
│   │   ├── survey_crud.py
│   │   └── recommendation_crud.py
│   ├── db/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── survey.py
│   │   └── recommendation.py
│   ├── schemas/
│   │   └── survey.py
│   └── services/
│       └── prompt_builder.py   # 설문 → Gemini 프롬프트 생성 함수
```

---

## ⚙️ 실행 방법

### 1. `.env` 파일 설정

```env
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/travia
GOOGLE_API_KEY=your_google_api_key
```

---

### 2. 패키지 설치 및 가상환경 실행

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

---

### 3. 테이블 생성 (최초 1회)

```bash
cd F:\trivia
set PYTHONPATH=.
python app/db/init_db.py
```

---

### 4. 서버 실행

```bash
uvicorn app.main:app --reload
```

---

## 🔌 API 명세

### ✅ POST `/api/v1/survey/recommend`  
설문을 저장하고 → Gemini 호출 → 추천 결과도 저장

#### 요청 예시

```json
{
  "username": "lee",
  "preferences": {
    "companion": "커플",
    "style": "감성, 먹방",
    "duration": "4박 5일",
    "driving": "불가능",
    "budget": "1500000원",
    "climate": "따뜻한 곳",
    "continent": "동남아",
    "density": "적당히"
  }
}
```

#### 응답 예시

```json
{
  "status": "success",
  "survey_id": 1,
  "recommendation_id": 1,
  "data": [
    {
      "city": "치앙마이",
      "country": "태국",
      "schedule": {
        "day_1": [...],
        "day_2": [...],
        ...
      }
    }
  ]
}
```

---

## 🗃️ 데이터베이스 구조

### 📌 `survey` 테이블

| 컬럼 | 타입 | 설명 |
|------|------|------|
| id | int (PK) | 설문 ID |
| username | string | 사용자명 |
| preferences | JSON | 설문 응답 전체 |
| created_at | timestamp | 생성일시 |

---

### 📌 `recommendation` 테이블

| 컬럼 | 타입 | 설명 |
|------|------|------|
| id | int (PK) | 추천 ID |
| survey_id | int (FK) | 설문 ID |
| result | JSON | AI 추천 결과 |
| created_at | timestamp | 생성일시 |

---

## 💬 기타

- API 테스트는 [Postman](https://www.postman.com/) 또는 Swagger UI(`http://localhost:8000/docs`) 사용 가능
- Gemini 응답 포맷은 JSON이며, `city`, `reason`, `schedule` 포함

---
