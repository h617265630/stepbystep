
### 根据字段，id,title,description,file_path,file_size,duration,uploader_id,uploaded_time,status,category_id,生成一个Video模型的示例代码
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float 
from sqlalchemy.orm import relationship
from app.db.database import Base
class Video(Base):
    __tablename__ = "videos"

    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=False)  # in bytes
    duration = Column(Float, nullable=False)  # in seconds
    uploader_id = Column(String(50), nullable=True)
    uploaded_time = Column(DateTime, nullable=False)
    status = Column(String(20), default="processing")  # e.g., 'processing', 'available', 'deleted'
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    category = relationship("Category", backref="videos")

    def __repr__(self):
        return f"<Video(id={self.id}, title='{self.title}', status='{self.status}')>"                                     
