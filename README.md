# 🌍 Travia Backend

**AI-Based Global Travel Destination + Itinerary Recommendation Service일정 추천 서비스**
Travia is a recommendation service that automatically generates travel cities and daily schedules that match the user's preferences through Google Gemini API based on the user's simple survey responses.

---

## ✅ Key Features

- Store user survey responses in the database
- Automatically generate prompts from survey data
- Integrate with Google Gemini 1.5 Flash API
- City recommendation and itinerary generation
- Store and return the recommendation results
- User signup/login system with JWT authentication

---

## 🧱 Project Structure

```
Travia_BE/
├── .env                        # 환경 변수 설정 파일
├── gemini_api/
│   └── gemini_api_client.py    # Gemini API 호출 및 JSON 파싱
├── app/
│   ├── main.py                 # FastAPI 앱 정의 및 라우터 등록
│   ├── api/v1/endpoints/
│   │   ├── survey.py           # 설문 + 추천 API 정의
│   │   └── auth.py           
│   ├── crud/
│   │   ├── survey_crud.py
│   │   ├── recommendation_crud.py
│   │   └── user_crud.py
│   ├── db/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── survey.py
│   │   ├── recommendation.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── survey.py
│   │   └── user.py
│   └── services/
│       └── prompt_builder.py   # 설문 → Gemini 프롬프트 생성 함수
```

---

## ⚙️ How to Run

### 1. Set up the `.env` file

```env
DATABASE_URL="mysql+pymysql://root:yourpassword@localhost:3306/travia"
GOOGLE_API_KEY="your_google_api_key"
```

---

### 2. Set up virtual environment and install packages

> On Debian/Ubuntu, install `python3-venv` first.
> If `python` doesn’t work, try using `python3`.

```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux
pip install -r requirements.txt
```

---

### 3. Initialize database tables (run once)

> Replace `F:\travia` with the actual project path on your machine

```bash
cd F:\trivia
set PYTHONPATH=.               # Windows
export PYTHONPATH=.            # Linux
python app/db/init_db.py
```

---

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

---

## 🔌 API Specification

### ✅ POST `/api/v1/survey/recommend`  
Saves the survey → Calls Gemini → Saves and returns recommendation

### ✅ POST `/api/v1/auth/login`
Authenticate user and issue JWT token

### ✅ POST `/api/v1/auth/signup`
Register a new user account

#### Sample Request

```json
{
  "username": "lee",
  "preferences": {
    "companion": "Couple",
    "style": "Emotional, Foodie",
    "duration": "5 days 4 nights",
    "driving": "No",
    "budget": "1,500,000 KRW",
    "climate": "Warm",
    "continent": "Southeast Asia",
    "density": "Moderate"
  }
}
```

#### Sample Response

```json
{
  "status": "success",
  "survey_id": 1,
  "recommendation_id": 1,
  "data": [
    {
      "city": "Chiang Mai",
      "country": "Thailand",
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

## 🗃️ Database Schema

### 📌 `survey` Table

| Column | Type | Description |
|------|------|------|
| id | int (PK) | Survey ID |
| username | string | User nickname |
| preferences | JSON | Survey answers |
| created_at | timestamp | Creation timestamp |

---

### 📌 `recommendation` Table

| Column | Type | Description |
|------|------|------|
| id | int (PK) | Recommendation ID |
| survey_id | int (FK) | Related survey ID |
| result | JSON | Gemini recommendation |
| created_at | timestamp | Creation timestamp |

---

## 💬 Notes

- You can test the API using [Postman](https://www.postman.com/) or Swagger UI at (`http://localhost:8000/docs`)
- Gemini responses are in JSON format, including `city`, `reason`, `schedule`

---
