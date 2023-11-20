from dataclasses import dataclass


@dataclass
class TokenData:
    access_token: str
    token_type: str = "Bearer"
    expires_in: int
