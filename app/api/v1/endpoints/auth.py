from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user import UserSignup, UserLogin
from app.db.session import get_db
from app.crud import user_crud
from app.utils.jwt import create_access_token  # 🔑 토큰 발급 함수 임포트

router = APIRouter()

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    try:
        db_user = user_crud.create_user(db, user)
        token = create_access_token(data={"sub": user.nickname})
        return {"status": "success", "token": token}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Nickname already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.authenticate_user(db, user.nickname, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid nickname or password")
    
    # 🔐 토큰 생성
    token = create_access_token(data={"sub": db_user.nickname})
    return {"status": "success", "token": token}
