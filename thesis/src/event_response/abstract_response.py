import json
from abc import abstractmethod, ABCMeta
from typing import Dict, Any


class AbstractResponse(metaclass=ABCMeta):
    response: Dict[str, Any] = {}

    @abstractmethod
    def generate_response(self, message: str) -> None:
        pass

    def get_response(self) -> str:
        return json.dumps(self.response)
