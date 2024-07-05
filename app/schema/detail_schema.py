from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo

class DetailCreateRequest(BaseModel):
    #detail_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="detail _id")
    episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 id")
    user_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="사용자 _id")
    age: int = Field(..., example=13, description="나이")
    story_name: str = Field(..., example="코난", description="스토리 이름")
    order: int = Field(..., example=0, description="0부터 시작하는 에피소드의 몇 번째 detail인지")
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))

class WrongDetailRequest(BaseModel):
    episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 id")
    user_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="사용자 _id")
    selection: str = Field(..., example="선택지 내용", description="선택지 내용")
    content: str = Field(..., example="detail 내용", description="선택지를 고르는 detail 내용")
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))

class DetailGetRequest(BaseModel):
    episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 id")
    user_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="사용자 _id")

class GetAllDetailRequest(BaseModel):
    episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 id")