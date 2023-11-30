from abc import ABC, abstractmethod
from ..data_transfer_objects.username_password_auth_response_model \
    import UsernamePasswordAuthResponseModel


class UsernamePasswordAuthOutputBoundary(ABC):
    @abstractmethod
    def form_response(self,
                      response_data: UsernamePasswordAuthResponseModel) -> None:
        pass

    @property
    @abstractmethod
    def response(self):
        pass
