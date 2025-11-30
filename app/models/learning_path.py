from sqlalchemy import Column, Integer, String,DateTime,Boolean,Text
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime


class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    is_public = Column(Boolean, default=True)

    # relationships 
    #users - learning_paths 多对多关系
    users = relationship("User", secondary="user_learning_paths", back_populates="learning_paths")
    #path_items -learnging_paths 多对多关系
    path_items = relationship("PathItem", secondary="learning_path_path_item", back_populates="learning_paths")


    def __repr__(self):
        return f"<LearningPath(id={self.id}, title='{self.title}')>"