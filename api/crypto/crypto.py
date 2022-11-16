from fastapi import APIRouter, Depends
from core.fastapi.dependencies import PermissionDependency
from core.fastapi.schemas.response import ExceptionResponseSchema
from app.crypto.service.crypto import CryptoService
from api.crypto.requests.crypto import CryptoRequests

crypto_router = APIRouter()


@crypto_router.get(
    "/summaries",
    dependencies=[Depends(PermissionDependency([]))],
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Get all the markets and there summaries, \
        also fetch the details of each market"
)
async def summaries(crypto_req: CryptoRequests = Depends()):
    """
        API to fetch the summaries and markets details based on market name
    """
    return await CryptoService().get_market_summary_and_details(crypto_req.market)
