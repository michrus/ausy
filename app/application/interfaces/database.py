from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class UserDTO:
    username: str
    password_hash: str


class DatabaseAccess(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserDTO:
        ...
