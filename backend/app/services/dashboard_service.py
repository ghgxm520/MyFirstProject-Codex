from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.dashboard import DashboardMetrics


class DashboardService:
    """驾驶舱聚合服务。"""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def build_metrics(self) -> DashboardMetrics:
        """汇总实时指标。

        说明：当前先返回样例数据，后续可通过物化视图或时序库提升性能。
        """
        _ = self.db
        return DashboardMetrics(
            dau=1280,
            content_heat=872,
            conversion_rate=0.137,
            revenue_cent=509900,
        )
