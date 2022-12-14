from abc import ABC, abstractmethod
from typing import List

from fastapi import Request
from fastapi.openapi.models import APIKey, APIKeyIn
from fastapi.security.base import SecurityBase
from core.exceptions import CustomException


class PermissionDependency(SecurityBase):
    def __init__(self, permissions: List):
        self.permissions = permissions
        self.model: APIKey = APIKey(
            **{"in": APIKeyIn.header}, name="Authorization"
        )
        self.scheme_name = self.__class__.__name__

    async def __call__(self, request: Request):
        for permission in self.permissions:
            cls = permission()
            if not await cls.has_permission(request=request):
                raise cls.exception


class BasePermission(ABC):
    exception = CustomException

    @abstractmethod
    async def has_permission(self, request: Request) -> bool:
        pass
