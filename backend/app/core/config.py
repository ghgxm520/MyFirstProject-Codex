from pydantic import BaseModel


class Settings(BaseModel):
    """应用配置；生产环境建议由环境变量或密钥管理服务注入。"""

    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/knowledge_hub"
    jwt_secret: str = "replace-me"
    jwt_algorithm: str = "HS256"


settings = Settings()
