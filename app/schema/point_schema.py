from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


class DetectPointRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")
    question: str = Field(None, example="gpt 마지막 질문", description="gpt 마지막 질문")
    input: str = Field(None, example="maiko", description="사용자 입력")

class AllDetectPointRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")

class AddCluePointRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")
    episode_id: str = Field(..., example="667d499079e8f1760cd861f4", description="에피소드 id")
    is_hint: int = Field(..., example=1, description="0:힌트 사용x, 1:힌트 사용 O, 2: 정답 보기를 한 경우")
    clue_order: int = Field(..., example=1, description="에피 별 단서 순서")

class EpisodePointRequest(BaseModel):
    episode_id: str = Field(..., example="667d499079e8f1760cd861f4", description="에피소드 id")
    name: str = Field(..., example="kitae", description="사용자 이름")

class CluePointRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")
