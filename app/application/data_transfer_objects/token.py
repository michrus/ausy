from dataclasses import dataclass


@dataclass
class TokenData:
    token_value: str
    expiration_timestamp: int
    token_type: str = "Bearer"
