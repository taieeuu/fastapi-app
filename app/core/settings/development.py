import logging

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    
    debug: bool = True

    title: str = "Dev FastAPI application"

    logging_level: int = logging.DEBUG
    
    host_name: str = 'localhost'

    class Config(AppSettings.Config):
        env_file = ".env"
