from src.event_handler.abstract_event_handler import AbstractEventHandler


class LaunchRequestHandler(AbstractEventHandler):

    def _handle_event(self) -> None:
        self.response_generator.generate_response("Launch request invoked correctly.")

