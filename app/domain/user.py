
class User:

    def __init__(self, username: str, password_hash: str) -> None:
        self._username = username
        self._password_hash = password_hash

    def validate_password(self, input_password: str):
        input_password_hash = self._hash_password(input_password)
        return input_password_hash == self._password_hash

    def _hash_password(self, password: str) -> str:
        ...
