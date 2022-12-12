from .log_informations import ENDPOINT_UNREACHABLE, INTERNAL_ERROR


class EndpointError(Exception):

    def __init__(self, msg: str = ENDPOINT_UNREACHABLE) -> None:
        Exception.__init__(self, msg)


class UserOperationError(Exception):

    def __init__(self, msg: str = INTERNAL_ERROR) -> None:
        Exception.__init__(self, msg)
