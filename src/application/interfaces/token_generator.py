from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Any

from ..data_transfer_objects.token import TokenData


class TokenGenerator(ABC):

    def __init__(self, secret_key: str, expiration_period: timedelta) -> None:
        self._secret_key = secret_key
        self._expiration_period = expiration_period

    @abstractmethod
    def generate(self, payload: dict[str, Any]) -> TokenData:
        ...
