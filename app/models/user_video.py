from sqlalchemy import Column, Integer, ForeignKey,Boolean,String
from app.db.database import Base
from sqlalchemy.orm import relationship

class UserVideo(Base):
    __tablename__ = 'user_video'
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    video_id = Column(Integer, ForeignKey('videos.id'), primary_key=True)
    liked = Column(Boolean, default=False)

    views_count = Column(Integer, default=0)
    is_public=Column(Boolean, default=True)
    status = Column(String(20), default="processing")  # e.g., 'processing', 'available', 'deleted'

       # 关系：一个用户与视频的关联
    user = relationship("User", back_populates="videos")
    video = relationship("Video", back_populates="users")