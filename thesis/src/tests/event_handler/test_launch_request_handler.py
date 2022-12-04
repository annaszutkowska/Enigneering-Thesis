from unittest import TestCase

from mock.mock import MagicMock

from .test_event_handler_data import response, launch_request
from thesis.src.event_handler.launch_request_handler import LaunchRequestHandler


class TestLaunchRequestHandler(TestCase):

    def setUp(self) -> None:
        self.handler = LaunchRequestHandler(launch_request)
        self.response = response

    def test__handle_event(self) -> None:
        self.handler.response_generator.generate_response = MagicMock()
        self.handler._handle_event()
        self.handler.response_generator.generate_response.assert_called_once_with("Launch request invoked correctly.")

