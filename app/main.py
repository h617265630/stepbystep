from fastapi import FastAPI
from app.routers import user
from app.db.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

app.include_router(user.router)
