from enum import Enum
from pydantic import Field
from pydantic_settings  import BaseSettings
from functools import lru_cache

class AppEnvTypes(Enum):
    prod: str = "prod"
    uat: str = "uat"
    dev: str = "dev"


class RedisSettings(BaseSettings):
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")
    redis_pwd: str = Field(..., env="REDIS_PWD")
    redis_db: str = Field(..., env="REDIS_DB")

class MongodbSettings(BaseSettings):
    mongo_host: str = Field(..., env="MONGO_HOST")
    mongo_db: str = Field(..., env="MONGO_DB")
    mongo_user: str = Field(..., env="MONGO_USER")
    mongo_pwd: str = Field(..., env="MONGO_PWD")
    mongo_port: str = Field(..., env="MONGO_PORT")

class EnvSettings(BaseSettings):
    app_env: str = Field(..., env="APP_ENV")

class MsSqlSettings(BaseSettings):
    ms_host: str = Field(..., env="MS_HOST")
    ms_db: str = Field(..., env="MS_DB")
    ms_user: str = Field(..., env="MS_USER")
    ms_pwd: str = Field(..., env="MS_PWD")
    ms_port: str = Field(..., env="MONGO_PORT")

class BaseAppSettings(RedisSettings, MongodbSettings, EnvSettings, MsSqlSettings):

    class Config:
        env_file = ".env"

