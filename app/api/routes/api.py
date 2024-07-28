from fastapi import APIRouter
from app.api.routes import indicator

router = APIRouter()
router.include_router(indicator.router, prefix="/indicator", tags=["indicator"])
