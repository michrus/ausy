import os
import sqlite3
from typing import Any

from ...adapters.database.database_access import DatabaseAccess


class LowLevelEagerSQLite3Database(DatabaseAccess):
    def __init__(self, db_name: str, db_dir_path: str) -> None:
        super().__init__(db_name=db_name)
        self._db_path: str = os.path.join(db_dir_path, db_name)

    def get_by_column(self,
                      table_name: str,
                      column_name: str,
                      column_value: str) -> list[dict[str, Any]]:
        with sqlite3.connect(self._db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            query = f'''SELECT * FROM {table_name} WHERE {column_name} = ?'''
            cursor.execute(query, (column_value,))
            rows = cursor.fetchall()
        rows_as_dicts = [dict(r) for r in rows]
        return rows_as_dicts
