from  typing import Optional
from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id:int
    email:str

    class Config:
        from_attribute = True
    

class UserResponse(UserBase):
    id: int

    class Config:
        from_attribute = True
 
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
