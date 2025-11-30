from sqlalchemy import Column, Integer, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.dialects.postgresql import ENUM
from enum import Enum as PyEnum

# 定义一个枚举类型，用于区分 Video 和 Clip
class ItemType(PyEnum):
    VIDEO = "video"
    CLIP = "clip"

class UserItemLike(Base):
    __tablename__ = "user_item_likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    item_id = Column(Integer, nullable=False)  # PathItem 的 ID，指向 Video 或 Clip
    item_type = Column(ENUM(ItemType), nullable=False)  # 区分 Video 或 Clip
    
    # 关系
    user = relationship("User", back_populates="likes")
    
    def __repr__(self):
        return f"<UserItemLike(user_id={self.user_id}, item_id={self.item_id}, item_type={self.item_type})>"
