import logging
from typing import Any, Dict, List
# from loguru import logger
# from pydantic import PostgresDsn, SecretStr

from app.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI Application"
    version: str = "0.1.0"

    # database_url: PostgresDsn
    max_connection_count: int = 10
    min_connection_count: int = 10

    # secret_key: SecretStr

    api_prefix: str = "/api"

    # jwt_token_prefix: str = "Token"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    # loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    host_name: str = 'localhost'

    class Config:
        # 模型實例的字段進行賦值時驗證數據類型，可以確保在運行時數據的一致性和正確性。
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
