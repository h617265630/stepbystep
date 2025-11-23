# backend/app/crud/user.py
from sqlalchemy.orm import Session
from app import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.user.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.user.UserCreate):
    db_user = models.user.User(
        username=user.username,
        email=user.email,
        password=user.password  # 实际使用 bcrypt 加密，这里先简化
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
