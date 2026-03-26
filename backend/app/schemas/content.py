from datetime import datetime

from pydantic import BaseModel, Field


class ContentCreate(BaseModel):
    """内容创建参数：支持三大内容模型统一入参。"""

    title: str = Field(min_length=2, max_length=128)
    summary: str = Field(default="", max_length=255)
    body: str
    content_type: str
    tags: list[str] = Field(default_factory=list)
    author_id: int


class ContentRead(BaseModel):
    """内容出参结构。"""

    id: int
    title: str
    summary: str
    content_type: str
    tags: list[str]
    author_id: int
    created_at: datetime
