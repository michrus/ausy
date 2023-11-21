from dataclasses import dataclass


@dataclass
class UserData:
    id: str
    name: str
    email: str
    access_level: str


@dataclass
class UserHash:
    user_id: str
    password_hash: str
