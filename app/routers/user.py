# backend/app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserResponse
from app.curd.user import (
    get_user, get_users, create_user, get_user_by_username
)
from app import schemas,auth,curd
from app.deps import get_db_dep,get_current_user


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=schemas.user.UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: schemas.user.UserCreate, db: Session = Depends(get_db_dep)):
    # check existing
    if curd.user.get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    if curd.user.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = auth.hash_password(user_in.password)
    user = curd.user.create_user(db, username=user_in.username, email=user_in.email, password=hashed)
    return user

@router.post("/login", response_model=schemas.user.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_dep)):
    user = curd.user.get_user_by_username(db, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = auth.create_access_token(subject=str(user.id))
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.user.UserOut)
def read_current_user(current_user = Depends(get_current_user)):
    # current_user 来自 deps.get_current_user（SQLAlchemy User 实例）
    return current_user



@router.get("/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dep)):
    return get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db_dep)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
