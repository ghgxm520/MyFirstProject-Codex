from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.content import ContentCreate, ContentRead
from app.services.content_service import ContentService

router = APIRouter()


@router.get("", response_model=list[ContentRead])
async def list_contents(
    db: Annotated[AsyncSession, Depends(get_db)],
    category: str | None = Query(default=None, description="筛选内容分类"),
    tag: str | None = Query(default=None, description="筛选标签"),
) -> list[ContentRead]:
    """获取内容列表，支持分类与标签过滤。"""
    return await ContentService(db).list_contents(category=category, tag=tag)


@router.post("", response_model=ContentRead)
async def create_content(
    payload: ContentCreate,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> ContentRead:
    """创建内容，用于后台 CMS 的发布流程。"""
    return await ContentService(db).create_content(payload)
