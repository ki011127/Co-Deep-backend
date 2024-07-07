from pydantic import BaseModel, Field

class ClueCheckRequest(BaseModel):
    episode_id: str = Field(..., example="667d97b4439cb3535f247322", description="에피소드 id")
    name: str = Field(..., example="testimony", description="단서 이름")
    order: int = Field(..., example=1, description="단서 순서")

class UserClueRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    name: str = Field(..., example="kitae", description="사용자 이름")
    level: int = Field(..., example=1, description="난이도")