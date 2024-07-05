from pydantic import BaseModel, Field
from typing import Optional, List
class EpisodeCreateRequest(BaseModel):
    # episode_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="에피소드 _id")
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    level: int = Field(..., example=1, description="난이도")
    # order: int = Field(..., example=1, description="에피소드 순서")
    # content: str = Field(..., example="에피소드 줄거리", description="에피소드")
    # clue_ids: List[str] = Field(..., examples="[clue_id1, clue_id2]", description="에피소드에 등장할 단서 리스트") 
    # img: Optional[str] = Field(..., example="s3주소", description="에피소드 이미지")

class EpisodeOrderRequest(BaseModel):
    story_id: str = Field(..., example="667d499079e8f1760cd861f4", description="스토리 id")
    level: int = Field(..., example=1, description="난이도")
    order: int = Field(..., example=1, description="에피소드 순서")