from fastapi import APIRouter

from app.api.v1 import routes_admin, routes_content, routes_payment

# 聚合 v1 版本下的全部业务路由
api_router = APIRouter()
api_router.include_router(routes_content.router, prefix="/contents", tags=["contents"])
api_router.include_router(routes_payment.router, prefix="/payments", tags=["payments"])
api_router.include_router(routes_admin.router, prefix="/admin", tags=["admin"])
