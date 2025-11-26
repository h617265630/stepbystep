# backend/app/crud/user.py
from sqlalchemy.orm import Session
from app.models.User import User
from app.auth import hash_password
from app.schemas.user import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, username: str, email: str, password: str):
    # `password` here is expected to be already hashed by the caller.
    db_user = User(
        username=username,
        email=email,
        password=password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
