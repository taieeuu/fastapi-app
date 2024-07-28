from enum import Enum
from pydantic import Field
from pydantic_settings  import BaseSettings


class AppEnvTypes(Enum):
    prod: str = "prod"
    uat: str = "uat"
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: str = Field(..., env="APP_ENV")
    mongo_host: str = Field(..., env="MONGO_HOST")
    mongo_db: str = Field(..., env="MONGO_DB")
    mongo_user: str = Field(..., env="MONGO_USER")
    mongo_pwd: str = Field(..., env="MONGO_PWD")
    mongo_port: str = Field(..., env="MONGO_PORT")
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")
    redis_pwd: str = Field(..., env="REDIS_PWD")
    redis_db: str = Field(..., env="REDIS_DB")

    class Config:
        env_file = ".env"
