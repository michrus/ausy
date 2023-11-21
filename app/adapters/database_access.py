from abc import ABC, abstractmethod
from typing import Any


class DatabaseAccess(ABC):
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name

    @abstractmethod
    def get_by_column(self,
                      table_name: str,
                      column_name: str,
                      column_value: str) -> list[dict[str, Any]]:
        pass
