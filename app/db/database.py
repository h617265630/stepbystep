from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#port: 5432
DATABASE_URL = "postgresql://postgres:burn@localhost/db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def create_tables():
#     # 注意：需要先导入所有模型，然后创建表
#     from models.user import User
#     from models.video import Video
#     from models.relations import UserVideoLike
    
#     Base.metadata.create_all(bind=engine)