from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo

class DetailCreateRequest(BaseModel):
    #detail_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="detail _id")
    episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 id")
    content: str = Field(..., example="생성 내용~~", description="생성 내용")
    user_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="사용자 _id")
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))

class DetailGetRequest(BaseModel):
    episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 id")
    user_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="사용자 _id")