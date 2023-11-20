from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class UsernamePasswordAuthResponseModel:
    error_message: Optional[str]
    token: str
    token_type: str


class UsernamePasswordAuthOutputBoundary(ABC):

    @abstractmethod
    def form_response(self,
                      response_data: UsernamePasswordAuthResponseModel) -> None:
        pass
