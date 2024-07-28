from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.core.log_config import logger
import logging

async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    logging.error(f'HTTPException: {exc.detail}')
    logger.error(f'HTTPException: {exc.detail}')
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)

