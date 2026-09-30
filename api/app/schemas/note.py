from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = None


class NoteResponse(BaseModel):
    id: int
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True