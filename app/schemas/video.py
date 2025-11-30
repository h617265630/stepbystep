from typing import Optional
from pydantic import BaseModel



class VideoBase(BaseModel):
    title:str
    description: Optional[str] = None
    file_path:str
    file_size:int
    duration:float
    model_config={
        "from_attributes": True 
    }   

class VideoCreate(VideoBase):
    pass

class VideoUpdate(BaseModel):
    pass
    
    model_config={
        "from_attributes": True 
    }



class VideoResponse(VideoBase):
    id: int
    view_count:int
    created_at: str
    updated_at: str
    thumbnail_path: Optional[str] = None
    model_config={
        "from_attributes": True 
    }   
 
    