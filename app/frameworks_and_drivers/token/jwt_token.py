from ...application.interfaces.token_generator import TokenGenerator
from ...application.dataclasses.token import TokenData


class JWTToken(TokenGenerator):

    def generate(self) -> TokenData:
        ...
