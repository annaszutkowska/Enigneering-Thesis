from unittest import TestCase

from mock.mock import MagicMock

from tests.event_handler.test_event_handler_data import response, intent_request
from thesis.src.event_handler.intent_request_handler import IntentRequestHandler


class TestLaunchRequestHandler(TestCase):

    def setUp(self) -> None:
        self.handler = IntentRequestHandler(intent_request)
        self.response = response

    def test__handle_event(self) -> None:
        self.handler.response_generator.generate_response = MagicMock()
        self.handler.response_generator.generate_response = MagicMock()
        self.handler._handle_event()
        self.handler.response_generator.generate_response.assert_called_once_with("There are 1 modules. Their names are: Cannabis Vera.")

