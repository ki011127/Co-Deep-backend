from pydantic import BaseModel, Field

class ClueCheckRequest(BaseModel):
    episode_id: str = Field(..., example="667d97b4439cb3535f247322", description="에피소드 id")
    name: str = Field(..., example="testimony", description="단서 이름")
    num_of_try: int = Field(..., example=1, description="시도 횟수")
    order: int = Field(..., example=1, description="단서 순서")