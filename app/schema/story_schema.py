from pydantic import BaseModel, Field

class StoryCreateRequest(BaseModel):
    story_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="스토리 _id")
    title: str = Field(..., example="코난", description="스토리 제목")
    description: str = Field(..., example="3K의 비밀", description="스토리 소제목")
    