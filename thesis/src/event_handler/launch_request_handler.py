from .abstract_event_handler import AbstractEventHandler


class LaunchRequestHandler(AbstractEventHandler):

    def _handle_event(self) -> None:
        self.response_generator.generate_response("You launched Luna Scientific skill.")

