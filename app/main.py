from fastapi import FastAPI
from app.routers import user,video,clip
from app.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API",debug = True)

app.include_router(user.router)
app.include_router(video.router)
app.include_router(clip.router)