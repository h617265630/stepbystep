# 生成一个Categories模型的示例代码
from sqlalchemy import Column, Integer, String, Text, Boolean,DatetTime,ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base    
class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    code = Column(String(50), unique=True, index=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    level = Column(Integer, default=0)  # 0表示顶级分类
    description = Column(Text, nullable=True)
    is_leaf = Column(Boolean, default=1)  # 1表示是叶子节点，0表示不是叶子节点
    created_at = Column(DatetTime, nullable=False)

    parent = relationship("Category", remote_side=[id], backref="children")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', level={self.level})>"

    def get_full_path(self):
        """获取类别的完整路径"""
        path_parts = [self.name]
        current = self.parent
        while current:
            path_parts.insert(0, current.name)
            current = current.parent
        return ' / '.join(path_parts)