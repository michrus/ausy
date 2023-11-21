from .database_access import DatabaseAccess
from ...application.interfaces.data import DataAccess
from ...application.data_transfer_objects.user import UserData, UserHash


class MultiDatabaseAccess(DataAccess):
    def __init__(self,
                 user_data_access: DatabaseAccess,
                 user_data_table: str,
                 user_hash_access: DatabaseAccess,
                 user_hash_table: str) -> None:
        self._user_data_access = user_data_access
        self._user_data_table = user_data_table
        self._user_hash_access = user_hash_access
        self._user_hash_table = user_hash_table

    def get_user_by_username(self, username: str) -> UserData:
        raw_user_data = self._user_data_access.get_by_column(
            table_name=self._user_data_table,
            column_name="username",
            column_value=username
        )
        user_data_row = raw_user_data[0]
        user_data = UserData(id=user_data_row["user_id"],
                             name=user_data_row["username"],
                             email=user_data_row["email"],
                             access_level=user_data_row["access_level"])
        return user_data


    def get_hash_by_user_id(self, user_id: str) -> UserHash:
        raw_user_hash = self._user_data_access.get_by_column(
            table_name=self._user_hash_table,
            column_name="user_id",
            column_value=user_id
        )
        user_hash_row = raw_user_hash[0]
        user_hash = UserHash(user_id=user_hash_row["user_id"],
                             password_hash=user_hash_row["hash"])
        return user_hash
