from dataclasses import dataclass
from typing import Optional

from .token import TokenData


@dataclass
class UsernamePasswordAuthResponseModel:
    success: bool
    message: str
    user_id: str
    token: Optional[TokenData] = TokenData()
