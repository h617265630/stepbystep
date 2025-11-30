from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base

class UserLearningPaths(Base):
    __tablename__ = "user_learning_paths"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    learning_path_id = Column(Integer, ForeignKey('learning_paths.id'), primary_key=True)
