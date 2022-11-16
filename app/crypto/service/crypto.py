from utils.crypto_api import BittrexAPI

BITTREX_URL = "https://api.bittrex.com/v3/markets"


class CryptoService:
    """
        Service file for Crypto market API
    """

    async def get_market_summary_and_details(self, market):
        """
            Method to fetch the summaries of markets or details of single market
        """
        if market:
            url = f"{BITTREX_URL}/{market.lower()}/summary"
        else:
            url = f"{BITTREX_URL}/summaries"
        response = await BittrexAPI().get(url=url)
        return {'data': response, 'message': 'Successfully retrived details'}
