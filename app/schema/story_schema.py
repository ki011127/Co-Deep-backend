from pydantic import BaseModel, Field

class StoryCreateRequest(BaseModel):
    title: str = Field(..., example="코난", description="스토리 제목")
    description: str = Field(..., example="3K의 비밀", description="스토리 소제목")
    