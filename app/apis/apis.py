from fastapi import APIRouter
from app.apis.routes import (
    sample_debug_router,
    sample_router,
    sample_sql_router
)

router = APIRouter()

router.include_router(sample_debug_router.router,     prefix="/sample_debug_router",         tags=["sample_debug_router"])
router.include_router(sample_router.router,           prefix="/sample_router",               tags=["sample_router"])
router.include_router(sample_sql_router.router,       prefix="/sample_sql_router",           tags=["sample_sql_router"])
