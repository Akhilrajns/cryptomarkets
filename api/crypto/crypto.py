from fastapi import APIRouter, Depends
from core.fastapi.dependencies import PermissionDependency
from core.fastapi.schemas.response import ExceptionResponseSchema
from app.crypto.service.crypto import CryptoService

crypto_router = APIRouter()


@crypto_router.get(
    "/summaries",
    dependencies=[Depends(PermissionDependency([]))],
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Get all the markets and there summaries, \
        also fetch the details of each market"
)
async def summaries(market: str = ''):
    return await CryptoService().get_market_summary_and_details(market)
