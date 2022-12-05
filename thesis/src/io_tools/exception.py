from .log_informations import ENDPOINT_UNREACHABLE, INTERNAL_ERROR


class EndpointError(Exception):

    def __init__(self) -> None:
        Exception.__init__(self, ENDPOINT_UNREACHABLE)


class UserOperationError(Exception):

    def __init__(self, msg: str = INTERNAL_ERROR) -> None:
        Exception.__init__(self, msg)
