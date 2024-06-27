from pydantic import BaseModel, Field

class UserCreateRequest(BaseModel):
    user_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="사용자 _id")
    name: str = Field(..., example="김기태", description = "사용자 이름")
    age: int = Field(..., example=1, description="사용자 연령대")