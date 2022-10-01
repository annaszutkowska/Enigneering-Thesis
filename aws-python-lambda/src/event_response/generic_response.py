import json
from typing import Dict, Any, Optional


class GenericResponse:
    response: Dict[str, Any] = {'version': '1.0', 'sessionAttributes': None, 'response': {'outputSpeech': None}}

    def generate_response(self, message: str, session_attributes: Dict = None) -> None:
        speech = self._build_plain_speech(message)
        self.response['sessionAttributes'] = self._get_session_attributes(session_attributes)
        self.response['response']['outputSpeech'] = speech

    def get_response(self) -> str:
        return json.dumps(self.response)

    @staticmethod
    def _build_plain_speech(message: str) -> Dict[str, Any]:
        return {'type': "PlainText", 'text': message}

    @staticmethod
    def _get_session_attributes(session_attributes: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if session_attributes is None:
            session_attributes = {}
        return session_attributes
