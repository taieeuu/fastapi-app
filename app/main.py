from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.apis.errors.value_error import value_error_handler
from app.apis.errors.http_error import http_error_handler
from app.apis.errors.validation_error import http422_error_handler

from app.apis.apis import router as api_router
from app.core.config import get_app_settings
from app.db.connect_to_redis import RedisConnectionFactory
import logging
from app.core.log_config import logger
from contextlib import asynccontextmanager
import uuid
import redis

LOCK_KEY = "init:stocks:once"
LOCK_TTL = 300
LOCK_VAL = str(uuid.uuid4())

def acquire_lock(client, key, value, ttl):
    # NX + EX: same as SETNX + EXPIRE
    # return True: get lock
    return client.set(key, value, ex=ttl, nx=True)

def release_lock(client, key, value):
    with client.pipeline() as pipe:
        while True:
            try:
                pipe.watch(key)
                if pipe.get(key) == value.encode():
                    pipe.multi()
                    pipe.delete(key)
                    pipe.execute()
                pipe.unwatch()
                break
            except redis.exceptions.WatchError:
                continue

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("init redis connection pool")
    RedisConnectionFactory.get_pool()
    client = RedisConnectionFactory.get_client()
    # the redis is lazy connection, so we need to ping it to check if the connection is alive
    client.ping()

    # try to get the lock, only one worker will trigger the init
    got_lock = False
    try:
        got_lock = acquire_lock(client, LOCK_KEY, LOCK_VAL, LOCK_TTL)
        if got_lock:
            # you can set your celery task here
            logger.info("you can set your celery task here")
        else:
            logger.info("skip init: other worker has already triggered")
        yield
    finally:
        # if the init is fast, you can release the lock here
        if got_lock:
            release_lock(client, LOCK_KEY, LOCK_VAL)
        RedisConnectionFactory.cleanup()

def get_application() -> FastAPI:
    settings = get_app_settings()
    
    logging.getLogger().setLevel(settings.logging_level)

    application = FastAPI(**settings.fastapi_kwargs, lifespan=lifespan)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    logging.basicConfig(level=settings.logging_level)

    application.include_router(api_router, prefix=settings.api_prefix)

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(ValueError, value_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    return application


app = get_application()

@app.get("/")
def index():
    return {"message": "Hello World"}
