from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base

class VideoCategory(Base):
    __tablename__ = 'video_category'
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(Integer, ForeignKey('videos.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)
