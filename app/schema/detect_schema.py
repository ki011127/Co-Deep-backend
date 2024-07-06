from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


# class DetectInitRequest(BaseModel):
#     story_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="스토리 id")
#     name: str = Field(..., example="kitae", description="사용자 이름")
#     level: int = Field(..., example=1, description="난이도")
#     created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))

class DetectChatRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")
    input: Optional[str] = Field(None, example="maiko", description="사용자 입력")
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Seoul")))

class AllDetectChatRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")