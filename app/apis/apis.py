from fastapi import APIRouter
from app.apis.routes import (
    sample_router,
    sample_sql_router
)

router = APIRouter()

router.include_router(sample_router.router,           prefix="/sample_router",               tags=["sample_router"])
router.include_router(sample_sql_router.router,       prefix="/sample_sql_router",           tags=["sample_sql_router"])
