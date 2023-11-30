class User:

    def __init__(self,
                 user_id: str,
                 password_hash: str) -> None:
        self._user_id: str = user_id
        self._password_hash: str = password_hash

    def change_password(self, current_password: str, new_password: str) -> bool:
        self.validate_password(current_password)
        new_password_hash = self._hash_password(new_password)
        self._password_hash = new_password_hash

    def serialize(self) -> dict[str, str]:
        return {
            "user_id": self._user_id,
            "password_hash": self._password_hash
        }

    def validate_password(self, input_password: str) -> None:
        input_password_hash = self._hash_password(input_password)
        if input_password_hash != self._password_hash:
            raise UserWrongPasswordError()

    def _hash_password(self, password: str) -> str:
        ...

class UserException(Exception):
    """Generic exception for User class."""
    pass

class UserWrongPasswordError(UserException):
    """Raised when password validation fails."""
    pass
