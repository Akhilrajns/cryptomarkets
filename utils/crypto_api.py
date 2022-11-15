from abc import ABC, abstractmethod
from fastapi import status
import requests
import logging
from core.exceptions.base import BadRequestException
from core.config import config
import hmac
import hashlib
import time

logger = logging.getLogger(__name__)


class API(ABC):

    @abstractmethod
    async def get(self, url: str, headers: dict):
        pass

    @abstractmethod
    async def post(self, url: str, data: dict, headers: dict):
        pass


class BittrexAPI(API):

    async def get(self, url: str, headers: dict = {}):
        try:
            headers = await self.generate_headers(url=url)
            result = requests.get(url=url, headers=headers)
            if result.status_code == status.HTTP_200_OK:
                return result.json()
            else:
                raise BadRequestException(
                    message=result.json().get('code', '')
                )
        except Exception as error:
            message = error.message if isinstance(
                error, BadRequestException
            ) else str(error)
            logger.info(f"API raised error: {message}")
            raise BadRequestException(message=message)

    async def post(self, url: str, data: dict = {}, headers: dict = {}):
        """
            # TODO This method is not complete
        """
        try:
            headers = await self.generate_headers(url=url)
            result = requests.post(url=url, data=data, headers=headers)
            if result.status_code == status.HTTP_200_OK:
                return result.json()
            else:
                raise BadRequestException(
                    message=result.json().get('code', '')
                )
        except Exception as error:
            message = error.message if isinstance(
                error, BadRequestException
            ) else str(error)
            logger.info(f"API raised error: {message}")
            raise BadRequestException(message=message)

    async def generate_headers(self, url: str):
        """
            Generate the header params
        """
        nonce = str(int(time.time() * 1000))
        content_hash = hashlib.sha512(''.encode()).hexdigest()
        signature = hmac.new(
            f"{config.SECRET_KEY}".encode(),
            ''.join([nonce, url, 'GET', content_hash]).encode(),
            hashlib.sha512
        ).hexdigest()

        return {
            'Api-Timestamp': nonce,
            'Api-Key': f"{config.API_KEY}",
            'Content-Type': 'application/json',
            'Api-Content-Hash': content_hash,
            'Api-Signature': signature
        }
