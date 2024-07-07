from pydantic import BaseModel, Field

class UserCreateRequest(BaseModel):
    name: str = Field(..., example="김기태", description = "사용자 이름")