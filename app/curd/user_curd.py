# backend/app/crud/user.py
from sqlalchemy.orm import Session
from app.models.user import User
# from app.auth import hash_password
# from app.schemas.user import UserCreate
from typing import Optional,List
from sqlalchemy.orm import selectinload

class UserCURD:
    @staticmethod
    def get_user(db: Session, user_id: int)->Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str)->Optional[User]:
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str)->Optional[User]:
        return db.query(User).filter(User.email == email).first()


    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100)->List[User]:
        return db.query(User).offset(skip).limit(limit).all()


    @staticmethod
    def create_user(db: Session, username: str, email: str, hashed_password: str)->User:   
        # `password` here is expected to be already hashed by the caller.
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    