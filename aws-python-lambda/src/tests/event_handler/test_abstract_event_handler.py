import json
from unittest import TestCase

from mock.mock import MagicMock

from code.event_handler.abstract_event_handler import AbstractEventHandler
from tests.event_handler.test_event_handler_data import response, request


class SomeEventHandler(AbstractEventHandler):

    def _handle_event(self) -> None:
        self.response_generator.generate_response("Event Handler Test")


class TestAbstractEventHandler(TestCase):

    def setUp(self) -> None:
        self.handler = SomeEventHandler(request)
        self.response = response

    def test_get_response(self) -> None:
        self.assertEqual(json.dumps(self.response), self.handler.get_response())

    def test__handle_event(self) -> None:
        self.handler.response_generator.generate_response = MagicMock()
        self.handler._handle_event()
        self.handler.response_generator.generate_response.assert_called_once_with("Event Handler Test")

