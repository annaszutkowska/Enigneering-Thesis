import importlib

from .abstract_event_handler import AbstractEventHandler
from ..event_response.error_response import ErrorResponse
from ..io_tools.exception import UserOperationError


class IntentRequestHandler(AbstractEventHandler):
    intent_module = "src.custom_intent_handler"

    def _handle_event(self) -> None:
        module = importlib.import_module(self.intent_module, package="event_handler")
        intent_name = self.request["intent"]["name"]
        class_ = getattr(module, intent_name)
        intent = class_(self.request["intent"].get("slots"))
        try:
            self.response_generator.generate_response(
                intent.generate_response()
            )
        except UserOperationError as e:
            self.response_generator = ErrorResponse()
            self.response_generator.generate_response(str(e))

