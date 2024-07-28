from fastapi import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.core.log_config import logger
import logging

async def value_error_handler(_: Request, exc: ValueError) -> JSONResponse:
    logging.error(f'ValueError: {exc}')
    logger.error(f'ValueError: {exc}')
    return JSONResponse({"errors": [str(exc)]}, status_code=status.HTTP_400_BAD_REQUEST)
