from pydantic import BaseModel, Field
from typing import Optional


class CryptoRequests(BaseModel):
    market: Optional[str] = Field(min_length=4, max_length=15)
