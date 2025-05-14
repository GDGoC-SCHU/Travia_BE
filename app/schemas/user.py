from pydantic import BaseModel

class UserSignup(BaseModel):
    name: str
    nickname: str
    password: str

class UserLogin(BaseModel):
    nickname: str
    password: str
