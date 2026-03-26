from pydantic import BaseModel


class DashboardMetrics(BaseModel):
    """驾驶舱指标模型。"""

    dau: int
    content_heat: int
    conversion_rate: float
    revenue_cent: int
