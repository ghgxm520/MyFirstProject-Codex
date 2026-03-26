from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router


def create_app() -> FastAPI:
    """创建 FastAPI 应用实例并注册中间件与路由。"""
    app = FastAPI(
        title="Knowledge Hub API",
        version="0.1.0",
        description="面向知识付费平台的异步 API 服务",
    )

    # 允许前端在开发阶段跨域访问后端接口
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api/v1")

    return app


app = create_app()
