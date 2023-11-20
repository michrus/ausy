from abc import ABC, abstractmethod

from ..dataclasses.token import TokenData


class TokenGenerator(ABC):
    @abstractmethod
    def generate(self) -> TokenData:
        ...
