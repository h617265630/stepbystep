from  typing import Optional
from pydantic import BaseModel



class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    file_path:str
    file_size:int
    duration:float
    category_id: Optional[int] = None
    is_public: Optional[bool] = True

    model_config={
        "from_attributes": True 
    }   

class VideoCreate(VideoBase):
    owener_id:int  ## uploader id

class VideoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    is_public: Optional[bool] = None
    status: Optional[str] = None
    
    model_config={
        "from_attributes": True 
    }



class VideoResponse(VideoBase):
    id: int
    owner_id: int
    views_count: int
    created_at: str
    updated_at: str
    thumbnail_path: Optional[str] = None

    model_config={
        "from_attributes": True 
    }   
 
 ## uploader info
class VideoOutWithOwner(VideoResponse):
    owner_username:str
    owner_display_name: Optional[str] = None
    