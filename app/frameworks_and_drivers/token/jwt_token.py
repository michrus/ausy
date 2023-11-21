from datetime import datetime, timedelta
from typing import Any

import jwt

from ...application.interfaces.token_generator import TokenGenerator
from ...application.data_transfer_objects.token import TokenData


class JWTToken(TokenGenerator):

    def __init__(self,
                 secret_key: str,
                 expiration_period: timedelta,
                 algorithm: str = "HS256") -> None:
        super().__init__(secret_key=secret_key,
                         expiration_period=expiration_period)
        self._algorithm = algorithm

    def generate(self, payload: dict[str, Any]) -> TokenData:
        expiry_datetime = datetime.utcnow() + self._expiration_period
        expiry_timestamp = int(expiry_datetime.timestamp())
        p = payload | {"exp": expiry_timestamp}
        token: str = jwt.encode(p, self._secret_key, self._algorithm)
        token_data = TokenData(token_value=token,
                               expiration_timestamp=expiry_timestamp,
                               token_type="Bearer")
        return token_data
