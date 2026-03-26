from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.dashboard import DashboardMetrics
from app.services.dashboard_service import DashboardService

router = APIRouter()


@router.get("/dashboard", response_model=DashboardMetrics)
async def get_dashboard_metrics(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> DashboardMetrics:
    """返回管理驾驶舱核心指标：日活、热度、转化、收入。"""
    return await DashboardService(db).build_metrics()
