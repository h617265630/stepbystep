from sqlalchemy import Column, Integer, String,DateTime,Boolean,Text
from sqlalchemy.orm import relationship
from  app.db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    display_name = Column(String(100))
    avatar_url = Column(String(500))
    bio = Column(Text)
    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    is_active = Column(Boolean, default=1)  # 1 for active, 0 for inactive
    is_superuser = Column(Boolean, default=False)  # 1 for superuser, 0 for regular user
    
    #relationships
    videos = relationship("Video",back_populates="owner",cascade="all, delete-orphan")
    videos_likes = relationship("UserVideoLike",back_populates="user")

    #自引用关系
    following = relationship(
         "UserFollow",
         foreign_keys="UserFollow.follower_id",
         back_populates="follower_rel"
    )
    followers_rel = relationship(
        "UserFollow",
        foreign_keys="UserFollow.following_id",
        back_populates="following_rel"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
@property
def video_count(self):
    return len(self.videos)

@property
def followers_count(self):
    return len(self.followers_rel)
    
@property
def following_count(self):
    return len(self.following)
    
def __repr__(self):
    return f"<User(id={self.id}, username='{self.username}')>"