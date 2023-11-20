from ...application.interfaces.database import DatabaseAccess, UserDTO


class SQLite3Database(DatabaseAccess):

    def get_user_by_username(self, username: str) -> UserDTO:
        ...
