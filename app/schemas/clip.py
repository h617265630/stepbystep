from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ClipBase(BaseModel):
    title:str
    description: Optional[str] = None
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

class ClipUpdate(ClipBase):
    pass
    model_config={
        "from_attributes": True
    }

# 返还给 前端的用户信息,一般只返回简单信息
class ClipResponse(ClipBase):
    id:int
    create_time: datetime
    
    model_config={
        "from_attributes": True
    }

