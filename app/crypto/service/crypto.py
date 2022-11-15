from utils.crypto_api import BittrexAPI

BITTREX_URL = "https://api.bittrex.com/v3/markets"


class CryptoService:

    async def get_market_summary_and_details(self, market):
        if market:
            url = f"{BITTREX_URL}/{market.lower()}/summary"
        else:
            url = f"{BITTREX_URL}/summaries"
        return await BittrexAPI().get(url=url)
