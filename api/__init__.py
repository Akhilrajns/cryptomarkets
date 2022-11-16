from fastapi import APIRouter
from api.home.home import home_router
from api.crypto.crypto import crypto_router


router = APIRouter()
router.include_router(home_router, prefix="/api/v1/home", tags=["Home"])
router.include_router(crypto_router, prefix="/api/v1/crypto", tags=["Crypto"])


__all__ = ["router"]
