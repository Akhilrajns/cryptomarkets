import pytest
from unittest.mock import patch
import requests
from utils.crypto_api import BittrexAPI
from core.exceptions.base import BadRequestException


@pytest.mark.asyncio
@patch.object(requests, 'get')
async def test_bittrex_api(mocker):
    """
        Test the BittrexAPI get method
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

    def res():
        r = requests.Response()
        r.status_code = 200

        def json_func():
            return response
        r.json = json_func
        return r
    mocker.return_value = res()
    org_response = await BittrexAPI().get(
        url='http://test.com', headers={}
    )
    assert org_response == response


@pytest.mark.asyncio
@patch.object(requests, 'get')
async def test_bittrex_api_with_exception(mocker):
    """
        Test the BittrexAPI get method
    """
    response = {'code': 'API_FAILED'}

    def res():
        r = requests.Response()
        r.status_code = 400

        def json_func():
            return response
        r.json = json_func
        return r
    mocker.return_value = res()
    with pytest.raises(BadRequestException):
        await BittrexAPI().get(
            url='http://test.com', headers={}
        )
