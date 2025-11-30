from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.curd.videoCrud import VideoCRUD

from app.schemas.video import VideoCreate, VideoResponse
from app.core.deps import get_db_dep,get_current_user
from typing import List

router = APIRouter(prefix="/videos", tags=["Videos"])

@router.post("/", response_model=VideoResponse, status_code=status.HTTP_201_CREATED)
def create_video(video_in: VideoCreate, db: Session = Depends(get_db_dep), current_user = Depends(get_current_user)):
    video = VideoCRUD.create_video(db,video_in,owner_id=current_user.id)

    # user = curd.user.create_user(db, username=user_in.username, email=user_in.email, password=hashed) 作比较
    return video

@router.get("/", response_model=List[VideoResponse])
def read_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dep)):
    videos = VideoCRUD.get_videos(db, skip=skip, limit=limit)
    return videos


@router.get("/{video_id}", response_model=VideoResponse)
def read_video(video_id: int, db: Session = Depends(get_db_dep)):
    db_video = VideoCRUD.get_video(db, video_id)
    if not db_video:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

# 暂时没有这个功能
# @router.put("/{video_id}", response_model=schemas.video.VideoResponse)
# def update_video(video_id: str, video_in: VideoUpdate, db: Session = Depends(get_db_dep), current_user: User = Depends(get_current_user)):
#     video = VideoCRUD.get_video(db, video_id)
#     if not video:
#         raise HTTPException(status_code=404, detail="Video not found")
#     if video.owner_id != current_user.id:
#         raise HTTPException(status_code=403, detail="Not authorized to update this video")
    
#     updated_video = VideoCRUD.update_video(db, video, video_in)
#     return updated_video

@router.delete("/{video_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_video(video_id: int, db: Session = Depends(get_db_dep), current_user = Depends(get_current_user)):
    video = VideoCRUD.get_video(db, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    if video.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this video")
    
    VideoCRUD.delete_video(db, video)
    return None