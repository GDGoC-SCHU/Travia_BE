from pydantic import BaseModel

# app/schemas/user.py
class UserSignup(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

