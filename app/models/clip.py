#根据以下字段生成clip的模型：id，title,description,clip_path, from_video_id,start_time,end_time,clip_duration,clip_method,generated_by,createdtime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.database import Base
class Clip(Base):
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    clip_path = Column(String(500), nullable=False)
    start_time = Column(Float, nullable=False)  # in seconds
    end_time = Column(Float, nullable=False)    # in seconds
    clip_duration = Column(Float, nullable=False)  # in seconds
    clip_method = Column(String(50), nullable=False)  # e.g., 'manual', 'automatic'
    generated_by = Column(String(50), nullable=True)
    created_time = Column(DateTime, nullable=False)

    # key
    from_video_id = Column(Integer, ForeignKey('videos.id'), nullable=False)
    
    #relationships
    video = relationship("Video", backref="clips")

    def __repr__(self):
        return f"<Clip(id={self.id}, title='{self.title}', from_video_id='{self.from_video_id}')>"