# app/auth.py
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from typing import Optional

# 密钥请替换为一个强随机字符串，或从环境变量读取
SECRET_KEY = "replace-this-with-a-very-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # token 有效期（分钟）

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = {"sub": str(subject)}
    now = datetime.now()
    expire = now + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"iat": now, "exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
