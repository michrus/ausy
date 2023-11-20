from dataclasses import dataclass


@dataclass
class UserData:
    id: str
    password_hash: str
    name: str
    email: str
