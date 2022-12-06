from .abstract_event_handler import AbstractEventHandler


class SessionEndedRequestHandler(AbstractEventHandler):

    def _handle_event(self) -> None:
        self.response_generator.generate_response("Luna Scientific session ended.")

