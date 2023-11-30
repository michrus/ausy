from dataclasses import dataclass


@dataclass
class UserHash:
    user_id: str
    password_hash: str

@dataclass
class UserHashAlgorithm:
    user_id: str
    hash_algorithm: str
