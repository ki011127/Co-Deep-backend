from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


class StoryRankRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    level: int = Field(..., example=1, description="난이도")