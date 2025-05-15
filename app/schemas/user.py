from pydantic import BaseModel

class UserSignup(BaseModel):
    name: str
    id: str
    password: str

class UserLogin(BaseModel):
    id: str
    password: str
