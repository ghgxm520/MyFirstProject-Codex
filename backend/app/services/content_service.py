from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.entities import Content
from app.schemas.content import ContentCreate, ContentRead


class ContentService:
    """封装内容领域逻辑，便于后续扩展缓存与审计。"""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def list_contents(self, category: str | None, tag: str | None) -> list[ContentRead]:
        """按条件查询内容，并转换为前端可直接消费的结构。"""
        stmt = select(Content)
        if category:
            stmt = stmt.where(Content.content_type == category)
        if tag:
            stmt = stmt.where(Content.tags.contains(tag))

        rows = (await self.db.execute(stmt)).scalars().all()
        return [
            ContentRead(
                id=row.id,
                title=row.title,
                summary=row.summary,
                content_type=row.content_type.value,
                tags=row.tags.split(",") if row.tags else [],
                author_id=row.author_id,
                created_at=row.created_at,
            )
            for row in rows
        ]

    async def create_content(self, payload: ContentCreate) -> ContentRead:
        """创建新内容并返回标准化结果。"""
        row = Content(
            title=payload.title,
            summary=payload.summary,
            body=payload.body,
            content_type=payload.content_type,
            tags=",".join(payload.tags),
            author_id=payload.author_id,
        )
        self.db.add(row)
        await self.db.commit()
        await self.db.refresh(row)

        return ContentRead(
            id=row.id,
            title=row.title,
            summary=row.summary,
            content_type=row.content_type.value,
            tags=row.tags.split(",") if row.tags else [],
            author_id=row.author_id,
            created_at=row.created_at,
        )
