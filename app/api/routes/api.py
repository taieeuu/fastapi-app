from fastapi import APIRouter
from app.api.routes import indicator
from app.api.routes import as400_middle

router = APIRouter()
router.include_router(indicator.router, prefix="/indicator", tags=["indicator"])
router.include_router(as400_middle.router, prefix="/as400", tags=["as400"])