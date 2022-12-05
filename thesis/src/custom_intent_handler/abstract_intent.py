from abc import ABCMeta, abstractmethod
from typing import Dict, Any, Tuple

from .api_response import response
from ..io_tools.exception import UserOperationError
from ..io_tools.log_informations import MODULE_DOES_NOT_EXIST


class AbstractIntent(metaclass=ABCMeta):

    def __init__(self, intent_data: Dict[str, Any]):
        self.request_data = intent_data
        self._get_token()
        self._get_status()

    @staticmethod
    def _get_token() -> None:
        # TODO: implement getting token from Luna app
        print("Getting token...")

    def _get_status(self) -> None:
        self.response = response  # TODO: po co ta metoda

    @abstractmethod
    def generate_response(self) -> str:
        pass

    def _get_number_of_modules(self) -> int:
        return len(self.response)

    def _get_module_list(self) -> list[str]:
        module_count = self._get_number_of_modules()
        return [self.response[module]["name"] for module in range(module_count)]

    def _get_module_data(self) -> Tuple[str, int]:
        module_name = self.request_data.get("module_name", {}).get("value")
        if module_name:
            try:
                module_index = self._check_if_valid(module_name)
                return module_name, module_index
            except UserOperationError as e:
                raise e  # TODO match name a little better (The Levenshtein Distance)
        raise UserOperationError()

    def _check_if_valid(self, module_name: str) -> int:
        for position, module in enumerate(self._get_module_list()):
            if module_name.casefold() == module.casefold():
                return position
        raise UserOperationError(MODULE_DOES_NOT_EXIST)

    def _get_measurements(self, module_index: int, stat: str) -> int:
        return self.response[module_index]["measurements"].get(stat)
