from dataclasses import dataclass


@dataclass
class UserHash:
    user_id: str
    password_hash: str
