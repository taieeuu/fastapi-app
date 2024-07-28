from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core.settings.app import AppSettings
from app.schedulers.tasks import schedule_jobs



def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        schedule_jobs()
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        pass
    return stop_app
