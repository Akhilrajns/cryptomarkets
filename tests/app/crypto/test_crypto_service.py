import pytest

from app.crypto.service.crypto import CryptoService


@pytest.mark.asyncio
async def test_get_all_markets_summary(mocker):
    """
        Test the crypto market to fetch all the markets
    """
    response = [{
            "symbol": "1ECO-USDT",
            "high": "1.430100000000",
            "low": "1.372610000000",
            "volume": "885.26600000",
            "quoteVolume": "1227.12148578",
            "percentChange": "1.80",
            "updatedAt": "2022-11-15T14:59:17.217Z"
        }]
    mocker.patch(
        "utils.crypto_api.BittrexAPI.get",
        return_value=response
    )
    org_response = await CryptoService()\
        .get_market_summary_and_details(market='')
    assert 1 == len(org_response.get('data'))

@pytest.mark.asyncio
async def test_to_fetch_market_details(mocker):
    """
        Test the crypto market to fetch details of a market
    """
    response = {
        "symbol": "1ECO-USDT",
        "high": "1.430100000000",
        "low": "1.372610000000",
        "volume": "885.26600000",
        "quoteVolume": "1227.12148578",
        "percentChange": "1.80",
        "updatedAt": "2022-11-15T14:59:17.217Z"
    }
    mocker.patch(
        "utils.crypto_api.BittrexAPI.get",
        return_value=response
    )
    org_response = await CryptoService()\
        .get_market_summary_and_details(market='1ECO-USDT')
    assert '1ECO-USDT' == org_response.get('data').get('symbol')
