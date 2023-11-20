from dataclasses import dataclass

from ..application.interfaces.username_password_auth_response \
    import UsernamePasswordAuthOutputBoundary, UsernamePasswordAuthResponseModel


@dataclass
class AuthTokenResponseDTO:
    error: str
    access_token: str
    type: str


class AuthTokenPresenter(UsernamePasswordAuthOutputBoundary):
    """_summary_
    """

    def __init__(self, response_dto: AuthTokenResponseDTO) -> None:
        self._response_dto = response_dto

    def form_response(self,
                      response_data: UsernamePasswordAuthResponseModel) -> None:
        self._response_dto.error = response_data.error_message
        self._response_dto.access_token = response_data.token
        self._response_dto.type = response_data.token_type
