from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.errors.value_error import value_error_handler
from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler

from app.api.routes.api import router as api_router
from app.core.config import get_app_settings
# from app.core.events import create_start_app_handler, create_stop_app_handler
from app.core.config import *
# from app.core.log_config import logging_setting
import logging
from app.core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    settings = get_app_settings()
    
    logging.getLogger().setLevel(settings.logging_level)

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    logging.basicConfig(level=settings.logging_level)

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )
    application.add_event_handler("startup", create_start_app_handler(application, settings))
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(api_router, prefix=settings.api_prefix)


    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(ValueError, value_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)


    return application


app = get_application()

@app.get("/")
def index():
    return {"message": "Hello World"}
