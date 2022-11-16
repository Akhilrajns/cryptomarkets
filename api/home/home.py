from fastapi import APIRouter, Response, Depends

from core.fastapi.dependencies import PermissionDependency

home_router = APIRouter()


@home_router.get("/health", dependencies=[Depends(PermissionDependency([]))])
async def home():
    """
        API for validatiing the health of application
    """
    return Response(status_code=200)
