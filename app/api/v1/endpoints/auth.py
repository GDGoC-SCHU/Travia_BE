from app.models.user import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user import UserSignup, UserLogin
from app.db.session import get_db
from app.crud import user_crud

router = APIRouter()

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    try:
        db_user = user_crud.create_user(db, user)
        return {"status": "success", "user_id": db_user.id}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Nickname already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid nickname or password")
    return {
        "status": "success",
        "user_id": db_user.id,
        "username": db_user.username}

@router.get("/check-username", summary="username 중복 여부 확인")
def check_username(username: str, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.username == username).first()
    return {
        "username": username,
        "is_available": not bool(exists)  # 사용 가능하면 True
    }