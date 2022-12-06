from unittest import TestCase

from thesis.src.io_tools.exception import UserOperationError
from thesis.src.io_tools.log_informations import MODULE_DOES_NOT_EXIST, INTERNAL_ERROR
from .test_intent_data import intent_data, mock_response, wrong_intent_data
from thesis.src.custom_intent_handler.abstract_intent import AbstractIntent


class SomeIntent(AbstractIntent):

    def generate_response(self) -> str:
        return "Some Intent Response"


class TestAbstractAbstractIntent(TestCase):
    wrong_name = "Wrong Module Name"
    correct_name = "Cannabis Vera"

    def setUp(self) -> None:
        self.intent = SomeIntent(intent_data)
        self.intent.response = mock_response

    def test__get_number_of_modules(self) -> None:
        self.assertEqual(self.intent._get_number_of_modules(), 1)

    def test__get_module_list(self) -> None:
        self.assertEqual(self.intent._get_module_list(), [self.correct_name])

    def test_get_module_data_error(self) -> None:
        self.intent.request_data = wrong_intent_data
        with self.assertRaises(UserOperationError) as e:
            self.intent.get_module_data()
        self.assertEqual(str(e.exception), MODULE_DOES_NOT_EXIST.format(self.wrong_name))

    def test_get_module_data_match(self) -> None:
        self.intent.request_data = wrong_intent_data
        self.intent.request_data["module_name"]["value"] = "Cannabis Veera"
        self.assertEqual(self.intent.get_module_data()[0], self.correct_name)

    def test_get_module_data_empty(self) -> None:
        self.intent.request_data = {}
        with self.assertRaises(UserOperationError) as e:
            self.intent.get_module_data()
        self.assertEqual(str(e.exception), INTERNAL_ERROR)

    def test__check_if_valid(self) -> None:
        self.assertEqual(self.intent._check_if_valid(self.correct_name), 0)

    def test__check_if_valid_error(self) -> None:
        with self.assertRaises(UserOperationError) as e:
            self.intent._check_if_valid(self.wrong_name)
        self.assertEqual(str(e.exception), INTERNAL_ERROR)
