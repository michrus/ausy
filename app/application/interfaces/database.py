from abc import ABC, abstractmethod

from ..dataclasses.user import UserData


class DatabaseAccess(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserData:
        ...
