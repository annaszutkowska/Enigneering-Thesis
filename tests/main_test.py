from unittest import TestCase
from unittest.mock import patch, MagicMock

from main import print_hi


class TestMain(TestCase):
    name = 'Test'

    @patch('builtins.print')
    def test_print_hi(self, print_mock: MagicMock) -> None:
        print_hi(self.name)
        print_mock.assert_called_with(f'Hi, {self.name}')