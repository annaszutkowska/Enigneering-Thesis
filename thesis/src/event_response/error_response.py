from typing import Dict

from .generic_response import GenericResponse


class ErrorResponse(GenericResponse):

    def generate_response(self, error_msg: str, session_attributes: Dict = None, end_session: bool = False) -> None:
        message = self._build_error_message(error_msg)
        super(ErrorResponse, self).generate_response(message, session_attributes, end_session)

    @staticmethod
    def _build_error_message(error_msg: str = "") -> str:
        message = "Sorry, there was an error while handling the request. {}".format(error_msg)
        return message
