from ...application.interfaces.token import TokenGenerator


class JWTToken(TokenGenerator):

    def generate(self) -> str:
        ...
