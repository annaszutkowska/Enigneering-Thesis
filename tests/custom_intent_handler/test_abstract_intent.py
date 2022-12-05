from unittest import TestCase

from src.io_tools.log_informations import MODULE_DOES_NOT_EXIST
from thesis.src.io_tools.exception import UserOperationError
from .test_intent_data import intent_data, mock_response, wrong_intent_data
from thesis.src.custom_intent_handler.abstract_intent import AbstractIntent


class SomeIntent(AbstractIntent):

    def generate_response(self) -> str:
        return "Some Intent Response"


class TestAbstractAbstractIntent(TestCase):

    def setUp(self) -> None:
        self.intent = SomeIntent(intent_data)
        self.intent.response = mock_response

    def test__get_number_of_modules(self) -> None:
        self.assertEqual(self.intent._get_number_of_modules(), 1)

    def test__get_module_list(self) -> None:
        self.assertEqual(self.intent._get_module_list(), ["Cannabis Vera"])

    def test__get_module_data(self) -> None:
        # self.handler.response_generator.generate_response = MagicMock()
        # self.handler._handle_event()
        # self.handler.response_generator.generate_response.assert_called_once_with("Event Handler Test")
        pass

    def test__get_module_data_error(self) -> None:
        self.intent.request_data = wrong_intent_data
        with self.assertRaises(UserOperationError) as e:
            self.intent._get_module_data()
        self.assertEqual(str(e.exception), MODULE_DOES_NOT_EXIST)