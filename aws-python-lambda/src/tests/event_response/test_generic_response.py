import json
from unittest import TestCase

from mock.mock import MagicMock

from src.event_response.generic_response import GenericResponse


class TestGenericResponse(TestCase):

    def setUp(self) -> None:
        self.generic_response = GenericResponse()
        self.message = "Generic Response Test"
        self.plain_speech = {'type': "PlainText", 'text': self.message}
        self.response = {'version': '1.0', 'sessionAttributes': {},
                         'response': {'outputSpeech': self.plain_speech, "shouldEndSession": False}}
        self.session_attributes = {"sessionId": "amzn1.echo-api.session.70acaef7-c686-469b-a427-2831bb7fa412"}

    def test_get_response(self) -> None:
        self.assertEqual(self.generic_response.get_response(), json.dumps(self.response))

    def test_generate_response(self) -> None:
        self.generic_response._build_plain_speech = MagicMock(return_value=self.plain_speech)
        self.generic_response.generate_response(self.message)
        self.generic_response._build_plain_speech.assert_called_once_with(self.message)
        self.assertEqual(self.generic_response.response['sessionAttributes'], {})
        self.assertEqual(self.generic_response.response['response']['outputSpeech']['text'], self.message)

    def test__get_session_attributes(self) -> None:
        self.assertEqual(self.generic_response._get_session_attributes(None), {})
        self.assertEqual(self.generic_response._get_session_attributes(self.session_attributes), self.session_attributes)

