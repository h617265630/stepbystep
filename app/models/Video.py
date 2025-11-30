### 根据字段，id,title,description,file_path,file_size,duration,uploader_id,uploaded_time,status,category_id,生成一个Video模型的示例代码
from sqlalchemy import Column, Integer, String,Boolean, Text, DateTime, ForeignKey, Float 
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    file_size = Column(Integer, nullable=False)  # in bytes
    file_path = Column(String(500), nullable=False)
    thumbnail_path = Column(String(500))
    duration = Column(Float, nullable=False)  # in seconds
    views_count = Column(Integer, default=0)
    is_public=Column(Boolean, default=True)
    status = Column(String(20), default="processing")  # e.g., 'processing', 'available', 'deleted'
   
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    
    #外键
    owner_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    #relationships
    owner = relationship("User", back_populates="videos")
    category = relationship("Category", backref="videos")
    user_likes = relationship("UserVideoLike", back_populates="video", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Video(id={self.id}, title='{self.title}', status='{self.status}')>"                                     
