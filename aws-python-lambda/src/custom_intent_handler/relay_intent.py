from src.custom_intent_handler.abstract_intent import AbstractIntent


class RelayIntent(AbstractIntent):

    def generate_response(self) -> str:
        return "The {relay} is on/off"
