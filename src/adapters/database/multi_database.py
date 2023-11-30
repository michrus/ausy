import json

from .database_access import DatabaseAccess
from ...application.interfaces.data import DataAccess
from ...application.data_transfer_objects.user_hash \
    import UserHash
from ...application.data_transfer_objects.user_hash_algo \
    import UserHashAlgorithm


class MultiDatabaseAccess(DataAccess):
    def __init__(self,
                 user_hash_access: DatabaseAccess,
                 user_hash_table: str,
                 hash_algo_access: DatabaseAccess,
                 hash_algo_table: str) -> None:
        self._user_hash_access = user_hash_access
        self._user_hash_table = user_hash_table
        self._hash_algo_access = hash_algo_access
        self._hash_algo_table = hash_algo_table

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
        parameters = json.loads(hash_algo_row["algorithm_parameters"])
        user_hash_algo = UserHashAlgorithm(
            user_id=hash_algo_row["user_id"],
            hash_algorithm=hash_algo_row["hash_algorithm"],
            algorithm_parameters=parameters
        )
        return user_hash_algo
