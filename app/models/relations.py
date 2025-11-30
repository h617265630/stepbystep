from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime
import enum

# 点赞类型枚举
class LikeType(enum.Enum):
    LIKE = "like"
    LOVE = "love"
    HAHA = "haha"
    WOW = "wow"
    SAD = "sad"
    ANGRY = "angry"


# 用户-视频点赞关联表
class UserVideoLike(Base):
    __tablename__ = "user_video_likes"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"), primary_key=True)
    like_type = Column(Enum(LikeType), default=LikeType.LIKE)
    created_at = Column(DateTime, default=datetime.now)
    
    # 关系
    user = relationship("User", back_populates="video_likes")
    video = relationship("Video", back_populates="user_likes")
    
    def __repr__(self):
        return f"<UserVideoLike(user_id={self.user_id}, video_id={self.video_id})>"

class UserFollow(Base):
    __tablename__ = "user_follows"
    
    follower_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    following_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    
    # 关系（自引用）
    follower = relationship("User", foreign_keys=[follower_id], backref="following")
    following = relationship("User", foreign_keys=[following_id], backref="followers")