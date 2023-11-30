from abc import ABC, abstractmethod

from ..data_transfer_objects.user_hash import UserHash
from ..data_transfer_objects.user_hash_algo import UserHashAlgorithm


class DataAccess(ABC):
    @abstractmethod
    def get_hash_by_user_id(self, user_id: str) -> UserHash:
        pass

    @abstractmethod
    def get_hash_algo_by_user_id(self, user_id: str) -> UserHashAlgorithm:
        pass
