from ...application.interfaces.database import DatabaseAccess
from ...application.data_transfer_objects.user import UserData, UserHash


class SQLite3Database(DatabaseAccess):
    def get_user_by_username(self, username: str) -> UserData:
        ...

    def get_hash_by_username(self, username: str) -> UserHash:
        ...
