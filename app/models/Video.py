### 根据字段，id,title,description,file_path,file_size,duration,uploader_id,uploaded_time,status,category_id,生成一个Video模型的示例代码
from sqlalchemy import Column, Integer, String,Boolean, Text, DateTime, ForeignKey, Float 
from sqlalchemy.orm import relationship
from app.models.path_item import PathItem
from datetime import datetime

class Video(PathItem):
    __tablename__ = "videos"

    id = Column(Integer, ForeignKey('path_items.id'), primary_key=True)
    file_size = Column(Integer, nullable=False)  # in bytes
    file_path = Column(String(500), nullable=False)
    thumbnail_path = Column(String(500))
    duration = Column(Float, nullable=False)  # in seconds
    view_count = Column(Integer, default=0)
    #relationships
    categories = relationship("Category", secondary="video_category", back_populates="videos")
    users = relationship("User", secondary="user_video", back_populates="videos")
    watch_history = relationship("WatchHistory", back_populates="video")

    #clips
    def __repr__(self):
        return f"<Video(id={self.id}, title='{self.title}', status='{self.status}')>"                                     
