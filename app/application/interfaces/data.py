from abc import ABC, abstractmethod

from ..data_transfer_objects.user import UserData, UserHash


class DataAccess(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserData:
        ...

    @abstractmethod
    def get_hash_by_user_id(self, user_id: str) -> UserHash:
        ...
