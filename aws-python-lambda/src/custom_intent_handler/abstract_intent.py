from abc import ABCMeta


class AbstractIntent(metaclass=ABCMeta):

    def __init__(self):
        self._get_token()

    @staticmethod
    def _get_token() -> None:
        print("Getting token...")
