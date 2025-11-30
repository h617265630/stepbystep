from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base

class LearningPathPathItem(Base):
    __tablename__ = 'learning_path_path_item'
    
    id = Column(Integer, primary_key=True, index=True)
    learning_path_id = Column(Integer, ForeignKey('learning_paths.id'), primary_key=True)
    path_item_id = Column(Integer, ForeignKey('path_items.id'), primary_key=True)
