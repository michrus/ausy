import base64
import hashlib

import bcrypt

from ...application.interfaces.hash_algo import HashingAlgorithm


class BCryptHashingAlgorithm(HashingAlgorithm):
    def __init__(self, name: str, rounds: int, prefix: bytes) -> None:
        super().__init__(name=name)
        self._salt = bcrypt.gensalt(rounds=rounds, prefix=prefix)

    def hash(self, input: str) -> str:
        input_bytes = input.encode("utf-8")
        input_sha256 = hashlib.sha256(input_bytes).digest()
        input_base64 = base64.b64encode(input_sha256)
        hashed: bytes = bcrypt.hashpw(input_base64, self._salt)
        hashed_str: str = hashed.decode("utf-8")
        return hashed_str
