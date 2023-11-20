from dataclasses import dataclass
from typing import Optional

from .token import TokenData
from .user import UserData


@dataclass
class UsernamePasswordAuthResponseModel:
    success: bool
    message: str
    user: Optional[UserData] = UserData()
    token: Optional[TokenData] = TokenData()
