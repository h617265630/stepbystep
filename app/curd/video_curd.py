from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.video import Video
from app.models.user_video import UserVideo

class VideoCURD:
    @staticmethod
    def get_video(db: Session, video_id: int) -> Optional[Video]:
        return db.query(Video).filter(Video.id == video_id).first()
    
    @staticmethod
    def get_videos_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Video]:
        videos = db.query(Video).join(UserVideo,UserVideo.video_id==Video.id)\
                    .filter(UserVideo.user_id == user_id)\
                    .offset(skip)\
                    .limit(limit)\
                    .all()
        return videos
    
    @staticmethod
    def create_video(db: Session, file_path:str,title: str, user_id: int, description:str=None) -> Video:
        video = Video(file_path=file_path, title=title, description=description)
        db.add(video)
        db.commit()
        db.refresh(video)

        # 创建关联记录
        user_video = UserVideo(user_id=user_id, video_id=video.id)
        try:
            db.add(user_video)
            db.commit()
        except:
            db.rollback()
            raise Exception("This video is already associated with the user.")

        return video
    
    
    @staticmethod
    def delete_video(db: Session, video: Video) -> None:
        db.delete(video)
        db.commit() 