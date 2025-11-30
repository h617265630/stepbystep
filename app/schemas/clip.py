from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime

class ClipBase(BaseModel):
    title:str
    description: Optional[str] = None
    clip_path:str
    from_video_id:str
    start_time:float
    end_time:float
    clip_duration:float
    clip_method:str
    generated_by: Optional[str] = None

    model_config={
        "from_attributes": True
    }

class ClipCreate(ClipBase):
    pass

class ClipUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    clip_path: Optional[str] = None
    # from_video_id 通常不允许在更新时修改，根据业务逻辑决定是否包含
    # from_video_id: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    clip_duration: Optional[float] = None
    clip_method: Optional[str] = None
    generated_by: Optional[str] = None

    model_config={
        "from_attributes": True
    }

# 返还给 前端的用户信息,一般只返回简单信息
class ClipResponse(ClipBase):
    id:str
    create_time: datetime
    
    model_config={
        "from_attributes": True
    }

