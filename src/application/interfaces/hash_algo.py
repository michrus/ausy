from abc import ABC, abstractmethod
from typing import Any


class HashingAlgorithm(ABC):
    def __init__(self, name: str) -> None:
        self._name: str = name

    @abstractmethod
    def hash(self, input: str) -> str:
        ...

    @property
    def name(self) -> str:
        return self._name


class HashingAlgorithmFactoryInterface(ABC):
    @abstractmethod
    def get_hash_algo(self,
                      name: str,
                      parameters: dict[str, Any]) -> HashingAlgorithm:
        ...


class HashingAlgorithmFactoryException(Exception):
    pass
