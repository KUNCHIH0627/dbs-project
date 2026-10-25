from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class FaqCreate(BaseModel):
    # 先去掉前後空白，再檢查長度（這樣只輸入空格也會被擋下）
    model_config = ConfigDict(str_strip_whitespace=True)

    course: str = Field(min_length=1, max_length=50)
    category: Optional[str] = Field(default=None, max_length=50)
    question: str = Field(min_length=1, max_length=300)
    answer: str = Field(min_length=1)
    keywords: Optional[str] = None


class FaqResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    course: str
    category: Optional[str] = None
    question: str
    answer: str
    keywords: Optional[str] = None
    created_at: datetime