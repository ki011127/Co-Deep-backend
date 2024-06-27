from pydantic import BaseModel, Field

class ClueCreateRequest(BaseModel):
    clue_id: str = Field(..., example="c831d225-8367-4383-98fc-2f07481dfba6", description="clue_id")