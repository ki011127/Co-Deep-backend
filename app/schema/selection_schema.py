from pydantic import BaseModel, Field
from typing import Optional, List

class SelectionCreateRequest(BaseModel):
    selection_id: List[str] = Field(..., example=["c831d225-8367-4383-98fc-2f07481dfba6", "another-id"], description="선택지 id 리스트")