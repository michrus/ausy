from .database_access import DatabaseAccess
from ...application.interfaces.data import DataAccess
from ...application.data_transfer_objects.user \
    import UserHash, UserHashAlgorithm, UserSalt


class MultiDatabaseAccess(DataAccess):
    def __init__(self,
                 user_hash_access: DatabaseAccess,
                 user_hash_table: str,
                 hash_algo_access: DatabaseAccess,
                 hash_algo_table: str,
                 user_salt_access: DatabaseAccess,
                 user_salt_table: str) -> None:
        self._user_hash_access = user_hash_access
        self._user_hash_table = user_hash_table
        self._hash_algo_access = hash_algo_access
        self._hash_algo_table = hash_algo_table
        self._user_salt_access = user_salt_access
        self._user_salt_table = user_salt_table

    def get_hash_by_user_id(self, user_id: str) -> UserHash:
        raw_user_hash = self._user_hash_access.get_by_column(
            table_name=self._user_hash_table,
            column_name="user_id",
            column_value=user_id
        )
        user_hash_row = raw_user_hash[0]
        user_hash = UserHash(user_id=user_hash_row["user_id"],
                             password_hash=user_hash_row["hash"])
        return user_hash

    def get_hash_algo_by_user_id(self, user_id: str) -> UserHashAlgorithm:
        raw_hash_algo = self._hash_algo_access.get_by_column(
            table_name=self._hash_algo_table,
            column_name="user_id",
            column_value=user_id
        )
        hash_algo_row = raw_hash_algo[0]
        user_hash_algo = UserHashAlgorithm(
            user_id=hash_algo_row["user_id"],
            hash_algorithm=hash_algo_row["hash_algorithm"]
        )
        return user_hash_algo

    def get_salt_by_user_id(self, user_id: str) -> UserSalt:
        raw_user_salt = self._user_salt_access.get_by_column(
            table_name=self._user_salt_table,
            column_name="user_id",
            column_value=user_id
        )
        user_salt_row = raw_user_salt[0]
        user_salt = UserSalt(user_id=user_salt_row["user_id"],
                             password_salt=user_salt_row["salt"])
        return user_salt
