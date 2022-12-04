import importlib

from .abstract_event_handler import AbstractEventHandler


class IntentRequestHandler(AbstractEventHandler):
    intent_module = "thesis.src.custom_intent_handler"

    def _handle_event(self) -> None:
        module = importlib.import_module(self.intent_module)
        intent_name = self.request["intent"]["name"]
        class_ = getattr(module, intent_name)
        intent = class_(self.request["intent"].get("slots"))
        self.response_generator.generate_response(
            intent.generate_response()
        )
