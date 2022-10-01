from abc import ABCMeta, abstractmethod
from typing import Dict, Any

from src.event_response.generic_response import GenericResponse


class AbstractEventHandler(metaclass=ABCMeta):

    def __init__(self, request: Dict[str, Any]):
        self.response_generator = GenericResponse()
        self.request = request
        self._handle_event()

    def get_response(self) -> str:
        return self.response_generator.get_response()

    @abstractmethod
    def _handle_event(self) -> None:
        pass
