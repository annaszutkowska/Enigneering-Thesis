from unittest import TestCase

from mock.mock import MagicMock

from thesis.src.event_handler.session_ended_request_handler import SessionEndedRequestHandler
from .test_event_handler_data import response, launch_request


class TestSessionEndedRequestHandler(TestCase):

    def setUp(self) -> None:
        self.handler = SessionEndedRequestHandler(launch_request)
        self.response = response

    def test__handle_event(self) -> None:
        self.handler.response_generator.generate_response = MagicMock()
        self.handler._handle_event()
        self.handler.response_generator.generate_response.assert_called_once_with("Luna Scientific session ended.")

