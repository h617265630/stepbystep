from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy import and_, or_, func
from typing import List, Optional
from models.user import User
from models.video import Video
from models.relations import UserVideoLike, UserFollow, LikeType

class VideoCRUD:
    @staticmethod
    def get_video(db: Session, video_id: int) -> Optional[Video]:
        return db.query(Video).filter(Video.id == video_id).first()
    
    @staticmethod
    def get_videos_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Video]:
        return (db.query(Video)
                .filter(Video.owner_id == user_id)
                .offset(skip)
                .limit(limit)
                .all())
    
    @staticmethod
    def create_video(db: Session, title: str, owner_id: int, **kwargs) -> Video:
        video = Video(title=title, owner_id=owner_id, **kwargs)
        db.add(video)
        db.commit()
        db.refresh(video)
        return video
    
    @staticmethod
    def get_video_with_owner(db: Session, video_id: int) -> Optional[Video]:
        return (db.query(Video)
                .options(joinedload(Video.owner))
                .filter(Video.id == video_id)
                .first())
    
    @staticmethod
    def like_video(db: Session, user_id: int, video_id: int, like_type: LikeType = LikeType.LIKE) -> UserVideoLike:
        # 检查是否已经点赞
        existing_like = (db.query(UserVideoLike)
                        .filter(
                            UserVideoLike.user_id == user_id,
                            UserVideoLike.video_id == video_id
                        )
                        .first())
        
        if existing_like:
            # 更新点赞类型
            existing_like.like_type = like_type
        else:
            # 创建新点赞
            existing_like = UserVideoLike(
                user_id=user_id,
                video_id=video_id,
                like_type=like_type
            )
            db.add(existing_like)
        
        db.commit()
        db.refresh(existing_like)
        return existing_like