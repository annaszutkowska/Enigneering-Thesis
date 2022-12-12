from abc import ABCMeta, abstractmethod
from functools import cache
from typing import Dict, Any, Tuple

from requests import HTTPError

from ..io_tools.exception import UserOperationError, EndpointError
from ..io_tools.log_informations import MODULE_DOES_NOT_EXIST
from ..luna_api.api_handler import ApiHandler


class AbstractIntent(metaclass=ABCMeta):
    LEV_DISTANCE = 3

    def __init__(self, intent_data: Dict[str, Any]):
        self.request_data = intent_data
        try:
            self.connector = ApiHandler()
            self._get_status()
        except (HTTPError, EndpointError):
            raise EndpointError

    def _get_status(self) -> None:
        self.response = self.connector.get_module_list()

    @abstractmethod
    def generate_response(self) -> str:
        pass

    def _get_number_of_modules(self) -> int:
        return len(self.response)

    def _get_module_list(self) -> list[Dict]:
        module_count = self._get_number_of_modules()
        return [self.response[module] for module in range(module_count)]

    def get_module_data(self) -> Tuple[str, int]:
        module_name = self.request_data.get("module_name", {}).get("value")
        if module_name:
            try:
                module_id = self._check_if_valid(module_name)
                return module_name, module_id
            except UserOperationError:
                try:
                    module_match = self._find_match(module_name)
                    module_id = self._check_if_valid(module_match)
                    return module_match, module_id
                except UserOperationError:
                    raise UserOperationError(MODULE_DOES_NOT_EXIST.format(module_name))
        raise UserOperationError

    def _check_if_valid(self, module_name: str) -> int:
        for module in self._get_module_list():
            if module_name.casefold() == module["name"].casefold():
                return module["id"]
        raise UserOperationError

    def _get_measurements(self, module_id: int, stat: str) -> int:
        module_data = list(filter(lambda module: module['id'] == module_id, self.response))[0]
        return module_data["measurements"].get(stat)

    def _find_match(self, module_name: str) -> str:
        module_list = self._get_module_list()
        match = {"name": module_name, "distance": len(module_name)}
        for possible_match in module_list:
            new_dist = self._levenshtein_distance(module_name, possible_match["name"])
            if match["distance"] > new_dist:
                match["name"] = possible_match["name"]
                match["distance"] = new_dist
        if match["name"] == module_name or match["distance"] > self.LEV_DISTANCE:
            raise UserOperationError
        return match["name"]

    @staticmethod
    def _levenshtein_distance(module_name: str, match: str) -> int:
        @cache
        def _minimal_distance(first: int, second: int) -> int:
            if first == len(module_name) or second == len(match):
                return len(module_name) - first + len(match) - second
            if module_name[first] == match[second]:
                return _minimal_distance(first + 1, second + 1)
            return 1 + min(
                _minimal_distance(first, second + 1),
                _minimal_distance(first + 1, second),
                _minimal_distance(first + 1, second + 1)
            )
        return _minimal_distance(0, 0)
