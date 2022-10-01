import importlib

import src.event_handler
from src.event_handler.abstract_event_handler import AbstractEventHandler


class IntentRequestHandler(AbstractEventHandler):

    def _handle_event(self) -> None:
        module = importlib.import_module("src.event_handler")
        intent_name = self.request["intent"]["name"]
        class_ = getattr(module, intent_name)
        intent = class_()
        print("DONE")
        # self.response_generator.generate_response("Launch request invoked correctly.")