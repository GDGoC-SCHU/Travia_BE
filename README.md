# Travia API

Travia API is a FastAPI-based backend application designed to support user authentication, survey submissions, and AI-powered travel recommendations using Google Gemini.

## 🚀 Features

- 🧾 User Signup & Login (`/api/auth`)
- 📋 Travel Preference Survey Submission (`/api/v1/survey`)
- 🤖 AI-based Travel Recommendation (Gemini API)
- 🗃️ MySQL database integration
- 🔐 CORS support for frontend integration (e.g., React/Next.js)

---

## 🛠 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **SQLAlchemy**
- **MySQL**
- **Pydantic**
- **Google Gemini API** (for AI recommendations)

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd app
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL connection**:
   ```bash
   DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>:<port>/<dbname>"
   ```
   
5. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🔗 API Endpoints

### 🔐 Auth (`/api/auth`)

- `POST /signup` — Register a new user  
- `POST /login` — User login  
- `GET /check-username?username=foo` — Check if username is available  

### 📋 Survey + Recommendation (`/api/v1/survey`)

- `POST /recommend` — Submit survey and receive AI travel recommendation  
- `GET /history/{username}` — Retrieve all survey/recommendation pairs for a user  
- `GET /detail/{survey_id}` — Get survey + recommendation details  
- `DELETE /delete/{survey_id}` — Delete a survey and its recommendation  

---

## ⚙️ Project Structure

```
app/
├── api/            # API routers
├── crud/           # Database CRUD operations
├── db/             # DB session and init
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── services/       # Prompt builder, Gemini client
└── main.py         # App entry point
```

---

## 🧪 Testing

You can test API endpoints using:

- Swagger UI: `http://localhost:8000/docs`
- Postman or Curl
