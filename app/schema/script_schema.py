from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


class ScriptGetRequest(BaseModel):
    order: int = Field(..., example="1", description="스크립트 순서")