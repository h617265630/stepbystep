from fastapi import FastAPI
from app.routers import user,video
from app.db.database import engine, Base
# 在create_all 之前导入所有模型
from app.models.user import User
from app.models.category import Category
from app.models.video import Video


Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API",debug = True)

app.include_router(user.router)
app.include_router(video.router)