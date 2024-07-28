from app.core.settings.app import AppSettings
from typing import List


class ProdAppSettings(AppSettings):

    allowed_hosts: List[str] = ["*"]

    host_name: str = 'prod_host'

    class Config(AppSettings.Config):
        env_file = ".env"
