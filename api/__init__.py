from fastapi import APIRouter
from api.home.home import home_router


router = APIRouter()
router.include_router(home_router, prefix="/api/v1/home", tags=["Home"])


__all__ = ["router"]
