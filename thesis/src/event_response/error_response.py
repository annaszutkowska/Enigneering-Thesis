import json
from typing import Dict, Any

from .abstract_response import AbstractResponse
from ..io_tools.log_informations import INTERNAL_ERROR


class ErrorResponse(AbstractResponse):
    response: Dict[str, Any] = {
        "event": {
            "header": {
                "namespace": "Alexa",
                "name": "ErrorResponse",
                "messageId": "0011",
                "payloadVersion": "3"
            },
            "endpoint": {
                "endpointId": "Test"
            },
            "payload": {}
        }
    }

    def generate_response(self, message: str,
                          error_type: str = "INTERNAL_ERROR", error_message: str = INTERNAL_ERROR) -> None:
        self.response['event']['payload'] = self._build_payload(error_type, error_message)

    def get_response(self) -> str:
        return json.dumps(self.response)

    @staticmethod
    def _build_payload(error_type: str, message: str) -> Dict[str, Any]:
        return {'type': error_type, 'message': message}
