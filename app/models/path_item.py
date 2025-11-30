from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base


# 采用多模态或者继承的方式来实现 PathItem
class PathItem(Base):
    __tablename__ = "path_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    # 关系：PathItem 属于一个学习路径
    learning_path = relationship("LearningPath", secondary="learning_path_path_item", back_populates="path_items")
    
    def __repr__(self):
        return f"<PathItem {self.title}>"
